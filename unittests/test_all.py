# Copyright 2014-2017 Insight Software Consortium.
# Copyright 2004-2009 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0.
# See http://www.boost.org/LICENSE_1_0.txt

import os
import sys
import unittest
import platform

from . import declarations_tester
from . import gccxml_runner_tester
from . import project_reader_correctness_tester
from . import source_reader_tester
from . import start_with_declarations_tester
from . import templates_tester
from . import hierarchy_traveling
from . import patcher_tester
from . import complex_types_tester
from . import cached_source_file_tester
from . import namespace_matcher_tester
from . import cache_enums_tester
from . import non_copyable_classes_tester
from . import vector_traits_tester
from . import string_traits_tester
from . import declarations_cache_tester
from . import dependencies_tester
from . import remove_template_defaults_tester
from . import find_container_traits_tester
from . import better_templates_matcher_tester
from . import declaration_matcher_tester
from . import calling_convention_tester
from . import gccxml10184_tester
from . import gccxml10185_tester
from . import test_directory_cache
from . import test_overrides

testers = [
    declarations_tester,
    gccxml_runner_tester,
    project_reader_correctness_tester,
    source_reader_tester,
    start_with_declarations_tester,
    templates_tester,
    hierarchy_traveling,
    complex_types_tester,
    cached_source_file_tester,
    namespace_matcher_tester,
    cache_enums_tester,
    non_copyable_classes_tester,
    vector_traits_tester,
    string_traits_tester,
    declarations_cache_tester,
    dependencies_tester,
    better_templates_matcher_tester,
    declaration_matcher_tester,
    calling_convention_tester,
    gccxml10184_tester,
    gccxml10185_tester,
    test_directory_cache,
    remove_template_defaults_tester,
    patcher_tester,
    find_container_traits_tester,
    test_overrides,
]


if os.path.isfile("test_cost.log"):
    # Remove the cost log file when tests are run again.
    # See the parser_test_case which generates this file.
    os.remove("test_cost.log")  # pragma: no cover


def create_suite():
    main_suite = unittest.TestSuite()
    for tester in testers:
        main_suite.addTest(tester.create_suite())
    return main_suite


def run_suite():
    result = unittest.TextTestRunner(verbosity=2).run(create_suite())
    error_desc = 'EXCEPTION IN SAFE SELECT 9'
    all_errors = result.failures + result.errors
    for test_case, description in all_errors:
        if error_desc not in description:  # pragma: no cover
            return 1  # pragma: no cover
    return 0


if __name__ == "__main__":
    sys.exit(run_suite())
