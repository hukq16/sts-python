#include "Random.h"
#include <cstdint>
#include <algorithm>
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(sts_random,m){
    m.doc() = "pybind11 for sts_random";
    py::class_<java::Random>(m,"JavaRandom")
        .def(py::init<std::int64_t>())
        .def("nextInt",py::overload_cast<std::int32_t>(&java::Random::nextInt))
        .def("nextInt",py::overload_cast<>(&java::Random::nextInt))
        .def("next",&java::Random::next)
        .def("nextLong",&java::Random::nextLong);



    py::class_<sts::stsRandom>(m,"stsRandom")
        .def(py::init<std::int64_t>())
        .def(py::init<>())
        .def(py::init<std::int64_t,std::int32_t>())
        // .def("murmurHash3",py::overload_cast<std::uint64_t>(&sts::stsRandom::murmurHash3))
        .def("setCounter",&sts::stsRandom::setCounter)
        .def("randomBoolean",py::overload_cast<>(&sts::stsRandom::randomBoolean))
        .def("randomBoolean",py::overload_cast<float>(&sts::stsRandom::randomBoolean))
        .def("randomLong",&sts::stsRandom::randomLong)
        // .def("nextLong",py::overload_cast<std::uint64_t>(&sts::Random::nextLong))
        // .def("nextLong",py::overload_cast<>(&sts::Random::nextLong))
        // .def("nextDouble",&sts::Random::nextDouble)
        // .def("nextFloat",&sts::Random::nextFloat)
        // .def("nextBoolean",&sts::Random::nextBoolean)
        .def("random",py::overload_cast<std::int32_t>(&sts::stsRandom::random))
        .def("random",py::overload_cast<std::int32_t,std::int32_t>(&sts::stsRandom::random))
        .def("random",py::overload_cast<std::int64_t>(&sts::stsRandom::random))
        .def("random",py::overload_cast<std::int64_t,std::int64_t>(&sts::stsRandom::random))
        .def("random",py::overload_cast<>(&sts::stsRandom::random))
        .def("random",py::overload_cast<float>(&sts::stsRandom::random))
        .def("random",py::overload_cast<float,float>(&sts::stsRandom::random))
        // .def("nextInt",py::overload_cast<std::int32_t>(&sts::Random::nextInt))
        // .def("nextInt",py::overload_cast<>(&sts::Random::nextInt))
        // .def("setCounter",&sts::Random::setCounter)
        .def("copy",&sts::stsRandom::copy)
        .def_readwrite("counter",&sts::stsRandom::counter);



        py::class_<sts::RandomXS128>(m,"RandomXS128")
        .def(py::init<>())
        .def(py::init<std::int64_t>())
        .def(py::init<std::int64_t,std::int64_t>())
        .def("murMurHash3",&sts::RandomXS128::murmurHash3)
        // // .def("setCounter",&sts::RandomXS128::setCounter)
        .def("setState",&sts::RandomXS128::setState)
        .def("getState",&sts::RandomXS128::getState)
        .def("next",&sts::RandomXS128::next)
        .def("nextBytes",&sts::RandomXS128::nextBytes)
        .def("setSeed",&sts::RandomXS128::setSeed)
        .def("nextLong",py::overload_cast<>(&sts::RandomXS128::nextLong))
        .def("nextLong",py::overload_cast<std::int64_t>(&sts::RandomXS128::nextLong))
        .def("nextDouble",&sts::RandomXS128::nextDouble)
        .def("nextFloat",&sts::RandomXS128::nextFloat)
        .def("nextBoolean",&sts::RandomXS128::nextBoolean)
        .def("nextInt",py::overload_cast<std::int32_t>(&sts::RandomXS128::nextInt))
        .def("nextInt",py::overload_cast<>(&sts::RandomXS128::nextInt))
        .def_readwrite("seed0",&sts::RandomXS128::seed0)
        .def_readwrite("seed1",&sts::RandomXS128::seed1);



}