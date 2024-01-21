//
// Created by gamerpuppy on 6/24/2021.
//
#include <cstdint>
#include <algorithm>
#include <random>
#include <chrono>
#include <climits>
#ifndef STS_LIGHTSPEED_RANDOM_H
#define STS_LIGHTSPEED_RANDOM_H

namespace java
{

    class Random
    {
    private:
        std::int64_t seed;
        static constexpr std::int64_t multiplier = 0x5DEECE66DLL;
        static constexpr std::int64_t addend = 0xBLL;
        static constexpr std::int64_t mask = (1LL << 48) - 1;
        static constexpr double DOUBLE_UNIT = 0x1.0p-53; // 1.0 / (1L << 53)

        static std::int64_t initialScramble(std::int64_t seed)
        {
            return (seed ^ multiplier) & mask;
        }

    public:
        Random(std::int64_t seed) : seed(initialScramble(seed)) {}

        std::int32_t next(std::int32_t bits)
        {
            seed = (seed * multiplier + addend) & mask;
            return static_cast<std::int32_t>(static_cast<std::int64_t>(static_cast<std::uint64_t>(seed) >> (48 - bits)));
        }

        std::int32_t nextInt()
        {
            return next(32);
        }

        std::int32_t nextInt(std::int32_t bound)
        {
            std::int32_t r = next(31);
            std::int32_t m = bound - 1;
            if ((bound & m) == 0) // i.e., bound is a power of 2
                r = static_cast<std::int32_t>(((bound * static_cast<std::int64_t>(r)) >> 31));
            else
            {
                for (std::int32_t u = r;
                     u - (r = u % bound) + m < 0;
                     u = next(31))
                    ;
            }
            return r;
        }

        std::int64_t nextLong()
        {
            // it's okay that the bottom word remains signed.
            return ((static_cast<std::int64_t>(next(32))) << 32) + next(32);
        }
    };

    namespace Collections
    {

        template <typename ForwardIterator>
        void shuffle(ForwardIterator begin, ForwardIterator end, java::Random rnd)
        {
            auto size = static_cast<int32_t>(end - begin);

            for (int i = size; i > 1; i--)
            {
                std::swap(*(begin + i - 1), *(begin + rnd.nextInt(i)));
            }
        }

    }
}

namespace sts
{

    class RandomXS128
    {
    public:
        static constexpr double NORM_DOUBLE = 1.1102230246251565E-16;
        static constexpr double NORM_FLOAT = 5.9604644775390625E-8;
        static constexpr std::int64_t ONE_IN_MOST_SIGNIFICANT = static_cast<std::int64_t>(1) << 63;

        std::int64_t seed0;
        std::int64_t seed1;

        RandomXS128()
        {
            // setSeed((new java::Random())->nextInt());
            auto seed_new = std::chrono::high_resolution_clock::now().time_since_epoch().count();
            std::mt19937_64 generator(seed_new); // 使用一个64位的Mersenne Twister生成器

            // 定义随机数的分布范围
            std::uniform_int_distribution<std::int64_t> distribution(LLONG_MIN, LLONG_MAX);

            // 生成随机数
            std::int64_t random_number = distribution(generator);

            setSeed(random_number);
        }

        RandomXS128(std::int64_t seed)
        {
            setSeed(seed);
        }

        RandomXS128(std::int64_t seed0, std::int64_t seed1)
        {
            setState(seed0, seed1);
        }

        static constexpr std::int64_t murmurHash3(std::int64_t y)
        {
            std::uint64_t x = static_cast<std::uint64_t>(y);
            x ^= x >> 33;
            x *= static_cast<std::uint64_t>(-49064778989728563LL);
            x ^= x >> 33;
            x *= static_cast<std::uint64_t>(-4265267296055464877LL);
            x ^= x >> 33;
            return static_cast<std::int64_t>(x);
        }

        void setSeed(std::int64_t seed)
        {
            std::int64_t seed0 = murmurHash3(seed == 0 ? ONE_IN_MOST_SIGNIFICANT : seed);
            setState(seed0, murmurHash3(seed0));
        }

        void setState(std::int64_t seed0, std::int64_t seed1)
        {
            this->seed0 = seed0;
            this->seed1 = seed1;
        }

        std::int64_t getState(std::int32_t seed)
        {
            return seed == 0 ? seed0 : seed1;
        }

        std::int64_t nextLong()
        {
            std::int64_t s1 = seed0;
            std::int64_t s0 = seed1;
            seed0 = s0;
            s1 ^= s1 << 23;

            std::int64_t s1_1 = static_cast<std::int64_t>(static_cast<std::uint64_t>(s1) >> 17);
            std::int64_t s0_2 = static_cast<std::int64_t>(static_cast<std::uint64_t>(s0) >> 26);
            seed1 = s1 ^ s0 ^ s1_1 ^ s0_2;
            return seed1 + s0;
        }

        std::int32_t next(std::int32_t bits)
        {
            return static_cast<std::int32_t>(nextLong() & ((1LL << bits) - 1));
        }
        std::int32_t nextInt()
        {
            return static_cast<std::int32_t>(nextLong());
        }

        std::int32_t nextInt(std::int32_t n)
        {
            return static_cast<std::int32_t>(nextLong(static_cast<std::int64_t>(n)));
        }

        std::int64_t nextLong(std::int64_t n)
        {
            if (n > 0)
            {
                std::int64_t bits;
                std::int64_t value;
                do
                {
                    bits = static_cast<std::int64_t>(static_cast<std::uint64_t>(nextLong()) >> 1);
                    value = bits % n;
                } while ((bits - value + n - 1) < 0LL);
                return value;
            }
            else
            {
                return 0;
            }
        }

        double nextDouble()
        {
            double x = static_cast<double>(static_cast<std::uint64_t>(nextLong()) >> 11);
            return x * NORM_DOUBLE;
        }

        float nextFloat()
        {
            double x = static_cast<double>(static_cast<std::uint64_t>(nextLong()) >> 40);
            double d = static_cast<double>(x) * NORM_FLOAT;
            return static_cast<float>(d);
        }

        bool nextBoolean()
        {
            return ((nextLong() & 1L) != 0L);
        }

        void nextBytes(std::vector<unsigned char> &bytes)
        {
            int i = bytes.size();

            while (i != 0)
            {
                int n = i < 8 ? i : 8;

                for (int64_t bits = nextLong(); n-- != 0; bits >>= 8)
                {
                    bytes[--i] = static_cast<unsigned char>(bits);
                }
            }
        }
    };

    class stsRandom
    {
    public:
        std::int32_t counter;
        RandomXS128 randomXS128;

        stsRandom()
        {
            RandomXS128 teprandom1;
            stsRandom(static_cast<std::int64_t>(teprandom1.nextDouble() * double(9999L)), static_cast<std::int32_t>(teprandom1.nextInt(99 + 1)));
        }

        stsRandom(std::int64_t seed) : randomXS128(seed)
        {
            counter = 0;
        }

        stsRandom(std::int64_t seed, std::int32_t targetCounter) : randomXS128(seed)
        {
            counter = 0;
            for (int i = 0; i < targetCounter; i++)
            {
                random(999);
            }
        }

        stsRandom copy()
        {
            stsRandom copied;
            copied.randomXS128 = RandomXS128(this->randomXS128.getState(0), this->randomXS128.getState(1));
            copied.counter = this->counter;
            return copied;
        }

        void setCounter(int targetCounter)
        {
            if (counter < targetCounter)
            {
                int count = targetCounter - counter;

                for (int i = 0; i < count; ++i)
                {
                    randomBoolean();
                }
            }
        }
        std::int32_t random(std::int32_t range)
        {
            ++counter;
            return randomXS128.nextInt(range + 1);
        }

        std::int32_t random(std::int32_t start, std::int32_t end)
        {
            ++counter;
            return start + randomXS128.nextInt(end - start + 1);
        }

        std::int64_t random(std::int64_t range)
        {
            ++counter;
            double d = randomXS128.nextDouble() * static_cast<double>(range);
            return static_cast<std::int64_t>(d);
        }

        std::int64_t random(std::int64_t start, std::int64_t end)
        {
            ++counter;
            double d = randomXS128.nextDouble() * static_cast<double>(end - start);
            return start + static_cast<int64_t>(d);
        }

        float random()
        {
            ++counter;
            return randomXS128.nextFloat();
        }

        float random(float range)
        {
            ++counter;
            return randomXS128.nextFloat() * range;
        }

        float random(float start, float end)
        {
            ++counter;
            return start + randomXS128.nextFloat() * (end - start);
        }

        std::int64_t randomLong()
        {
            ++counter;
            return randomXS128.nextLong();
        }

        bool randomBoolean()
        {
            ++counter;
            return randomXS128.nextBoolean();
        }

        // std::int32_t nextInt(std::int32_t n) {
        //     return static_cast<std::int32_t>(nextLong(n));
        // }

        bool randomBoolean(float chance)
        {
            ++counter;
            return randomXS128.nextFloat() < chance;
        }
    };

}

#endif // STS_LIGHTSPEED_RANDOM_H
