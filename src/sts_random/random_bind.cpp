#include "Random.h"
#include <cstdint>
#include <algorithm>
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(sts_random,m){
    m.doc() = "pybind11 for sts_random";
    py::class_<java::Random>(m,"JavaRandom")
        .def(py::init<std::uint64_t>())
        .def("nextInt",py::overload_cast<std::int32_t>(&java::Random::nextInt))
        .def("nextInt",py::overload_cast<>(&java::Random::nextInt))
        .def("next",&java::Random::next);

    py::class_<sts::Random>(m,"stsRandom")
        .def(py::init<std::uint64_t>())
        .def(py::init<>())
        .def(py::init<std::uint64_t,std::int32_t>())
        .def("murmurHash3",py::overload_cast<std::uint64_t>(&sts::Random::murmurHash3))
        .def("setCounter",&sts::Random::setCounter)
        .def("randomBoolean",py::overload_cast<>(&sts::Random::randomBoolean))
        .def("randomBoolean",py::overload_cast<float>(&sts::Random::randomBoolean))
        .def("randomLong",&sts::Random::randomLong)
        .def("nextLong",py::overload_cast<std::uint64_t>(&sts::Random::nextLong))
        .def("nextLong",py::overload_cast<>(&sts::Random::nextLong))
        .def("nextDouble",&sts::Random::nextDouble)
        .def("nextFloat",&sts::Random::nextFloat)
        .def("nextBoolean",&sts::Random::nextBoolean)
        .def("random",py::overload_cast<std::int32_t>(&sts::Random::random))
        .def("random",py::overload_cast<std::int32_t,std::int32_t>(&sts::Random::random))
        .def("random",py::overload_cast<std::int64_t>(&sts::Random::random))
        .def("random",py::overload_cast<std::int64_t,std::int64_t>(&sts::Random::random))
        .def("random",py::overload_cast<>(&sts::Random::random))
        .def("random",py::overload_cast<float>(&sts::Random::random))
        .def("random",py::overload_cast<float,float>(&sts::Random::random))
        .def("nextInt",py::overload_cast<std::int32_t>(&sts::Random::nextInt))
        .def("nextInt",py::overload_cast<>(&sts::Random::nextInt))
        .def("setCounter",&sts::Random::setCounter)
        .def_readwrite("counter",&sts::Random::counter)
        .def_readwrite("seed0",&sts::Random::seed0)
        .def_readwrite("seed1",&sts::Random::seed1);


}