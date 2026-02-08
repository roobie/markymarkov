"""Auto-generated Semantic Markov model for code patterns"""

from collections import Counter
from enum import Enum


class CodePattern(Enum):
    """High-level semantic patterns."""

    IF_NONE_CHECK = "if-none-check"
    IF_NOT_NONE = "if-not-none"
    IF_EMPTY_CHECK = "if-empty-check"
    IF_TYPE_CHECK = "if-type-check"
    GUARD_CLAUSE = "guard-clause"
    EARLY_RETURN_SUCCESS = "early-return-success"
    EARLY_RETURN_FAILURE = "early-return-failure"
    LOOP_ACCUMULATE = "loop-accumulate"
    LOOP_TRANSFORM = "loop-transform"
    LOOP_FILTER = "loop-filter"
    LOOP_ENUMERATE = "loop-enumerate"
    LOOP_ZIP = "loop-zip"
    LOOP_DICT_ITEMS = "loop-dict-items"
    RETURN_NONE = "return-none"
    RETURN_BOOL = "return-bool"
    RETURN_LIST = "return-list"
    RETURN_DICT = "return-dict"
    RETURN_COMPUTED = "return-computed"
    INIT_EMPTY_LIST = "init-empty-list"
    INIT_EMPTY_DICT = "init-empty-dict"
    INIT_COUNTER = "init-counter"
    INIT_DEFAULT_VALUE = "init-default-value"
    APPEND_TO_LIST = "append-to-list"
    DICT_UPDATE = "dict-update"
    DICT_GET_DEFAULT = "dict-get-default"
    DEFAULT_DICT_PATTERN = "defaultdict-pattern"
    TRY_EXCEPT_PASS = "try-except-pass"
    TRY_EXCEPT_LOG = "try-except-log"
    TRY_EXCEPT_RERAISE = "try-except-reraise"
    TRY_FINALLY = "try-finally"
    CONTEXT_MANAGER = "context-manager"
    FUNCTION_VALIDATOR = "function-validator"
    FUNCTION_TRANSFORMER = "function-transformer"
    FUNCTION_FACTORY = "function-factory"
    INIT_METHOD = "init-method"
    PROPERTY_GETTER = "property-getter"
    PROPERTY_SETTER = "property-setter"
    CLASS_METHOD = "class-method"
    STATIC_METHOD = "static-method"
    FUNCTION_DECORATOR = "function-decorator"
    LIST_COMPREHENSION = "list-comprehension"
    DICT_COMPREHENSION = "dict-comprehension"
    GENERATOR_EXPRESSION = "generator-expression"
    API_VALIDATION = "api-validation"
    API_ERROR_RESPONSE = "api-error-response"
    API_SUCCESS_RESPONSE = "api-success-response"
    TERNARY_EXPRESSION = "ternary-expression"
    STRING_FORMAT = "string-format"
    LOGGING_CALL = "logging-call"
    UNPACKING = "unpacking"
    BOOLEAN_EXPRESSION = "boolean-expression"
    UNKNOWN = "unknown"


# Pattern transition counts
transitions = {
    (CodePattern.IF_EMPTY_CHECK, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.GENERATOR_EXPRESSION: 8,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.STRING_FORMAT: 128,
            CodePattern.CONTEXT_MANAGER: 62,
            CodePattern.UNPACKING: 25,
            CodePattern.FUNCTION_TRANSFORMER: 23,
            CodePattern.INIT_DEFAULT_VALUE: 22,
            CodePattern.RETURN_COMPUTED: 17,
            CodePattern.GENERATOR_EXPRESSION: 7,
            CodePattern.TERNARY_EXPRESSION: 6,
            CodePattern.LOOP_ACCUMULATE: 5,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.TRY_FINALLY: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 86,
            CodePattern.STRING_FORMAT: 69,
            CodePattern.INIT_DEFAULT_VALUE: 26,
            CodePattern.UNPACKING: 6,
            CodePattern.LOGGING_CALL: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 102,
            CodePattern.STRING_FORMAT: 63,
            CodePattern.INIT_DEFAULT_VALUE: 27,
            CodePattern.GENERATOR_EXPRESSION: 19,
            CodePattern.LIST_COMPREHENSION: 13,
            CodePattern.FUNCTION_TRANSFORMER: 9,
            CodePattern.UNPACKING: 7,
            CodePattern.DICT_GET_DEFAULT: 5,
            CodePattern.RETURN_COMPUTED: 4,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 43,
            CodePattern.FUNCTION_TRANSFORMER: 23,
            CodePattern.GUARD_CLAUSE: 11,
            CodePattern.INIT_EMPTY_LIST: 11,
            CodePattern.IF_TYPE_CHECK: 7,
            CodePattern.UNPACKING: 7,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.RETURN_LIST: 5,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.INIT_COUNTER: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 167,
            CodePattern.RETURN_NONE: 66,
            CodePattern.IF_EMPTY_CHECK: 26,
            CodePattern.FUNCTION_TRANSFORMER: 22,
            CodePattern.RETURN_LIST: 22,
            CodePattern.GUARD_CLAUSE: 19,
            CodePattern.RETURN_BOOL: 14,
            CodePattern.TERNARY_EXPRESSION: 13,
            CodePattern.UNPACKING: 13,
            CodePattern.IF_TYPE_CHECK: 8,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.LIST_COMPREHENSION: 7,
            CodePattern.RETURN_DICT: 7,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.TRY_EXCEPT_RERAISE: 5,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.TRY_EXCEPT_PASS: 3,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 136,
            CodePattern.RETURN_COMPUTED: 84,
            CodePattern.IF_EMPTY_CHECK: 28,
            CodePattern.INIT_DEFAULT_VALUE: 17,
            CodePattern.RETURN_LIST: 14,
            CodePattern.GUARD_CLAUSE: 12,
            CodePattern.TERNARY_EXPRESSION: 10,
            CodePattern.PROPERTY_GETTER: 10,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.IF_TYPE_CHECK: 7,
            CodePattern.LIST_COMPREHENSION: 7,
            CodePattern.UNPACKING: 7,
            CodePattern.INIT_METHOD: 5,
            CodePattern.LOOP_FILTER: 5,
            CodePattern.INIT_EMPTY_LIST: 5,
            CodePattern.FUNCTION_VALIDATOR: 4,
            CodePattern.TRY_EXCEPT_RERAISE: 4,
            CodePattern.CLASS_METHOD: 4,
            CodePattern.TRY_FINALLY: 3,
            CodePattern.STATIC_METHOD: 3,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.EARLY_RETURN_SUCCESS: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 45,
            CodePattern.FUNCTION_TRANSFORMER: 13,
            CodePattern.IF_EMPTY_CHECK: 11,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.UNPACKING: 4,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.RETURN_LIST: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 1359,
            CodePattern.FUNCTION_TRANSFORMER: 324,
            CodePattern.GUARD_CLAUSE: 226,
            CodePattern.IF_EMPTY_CHECK: 193,
            CodePattern.IF_NONE_CHECK: 135,
            CodePattern.UNPACKING: 98,
            CodePattern.IF_TYPE_CHECK: 81,
            CodePattern.INIT_EMPTY_LIST: 80,
            CodePattern.TERNARY_EXPRESSION: 78,
            CodePattern.INIT_DEFAULT_VALUE: 62,
            CodePattern.LIST_COMPREHENSION: 56,
            CodePattern.EARLY_RETURN_SUCCESS: 49,
            CodePattern.IF_NOT_NONE: 47,
            CodePattern.CONTEXT_MANAGER: 44,
            CodePattern.DICT_GET_DEFAULT: 43,
            CodePattern.RETURN_LIST: 35,
            CodePattern.INIT_EMPTY_DICT: 35,
            CodePattern.TRY_EXCEPT_RERAISE: 29,
            CodePattern.LOOP_ACCUMULATE: 28,
            CodePattern.RETURN_DICT: 25,
            CodePattern.INIT_COUNTER: 22,
            CodePattern.RETURN_BOOL: 22,
            CodePattern.STRING_FORMAT: 21,
            CodePattern.TRY_EXCEPT_PASS: 19,
            CodePattern.GENERATOR_EXPRESSION: 19,
            CodePattern.RETURN_NONE: 16,
            CodePattern.INIT_METHOD: 13,
            CodePattern.DICT_COMPREHENSION: 11,
            CodePattern.LOOP_DICT_ITEMS: 11,
            CodePattern.PROPERTY_GETTER: 8,
            CodePattern.LOGGING_CALL: 7,
            CodePattern.FUNCTION_VALIDATOR: 7,
            CodePattern.LOOP_FILTER: 5,
            CodePattern.TRY_FINALLY: 4,
            CodePattern.LOOP_ENUMERATE: 4,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 87,
            CodePattern.RETURN_NONE: 65,
            CodePattern.IF_NONE_CHECK: 14,
            CodePattern.INIT_EMPTY_LIST: 12,
            CodePattern.RETURN_LIST: 12,
            CodePattern.IF_EMPTY_CHECK: 11,
            CodePattern.INIT_EMPTY_DICT: 11,
            CodePattern.FUNCTION_TRANSFORMER: 9,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.DICT_GET_DEFAULT: 6,
            CodePattern.UNPACKING: 6,
            CodePattern.TRY_EXCEPT_RERAISE: 5,
            CodePattern.TRY_EXCEPT_PASS: 5,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.RETURN_BOOL: 4,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.GUARD_CLAUSE: 3,
            CodePattern.PROPERTY_GETTER: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 13,
            CodePattern.INIT_DEFAULT_VALUE: 11,
            CodePattern.IF_EMPTY_CHECK: 8,
            CodePattern.RETURN_COMPUTED: 7,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.IF_EMPTY_CHECK: 5,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.GENERATOR_EXPRESSION: 7,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 61,
            CodePattern.IF_EMPTY_CHECK: 11,
            CodePattern.LIST_COMPREHENSION: 11,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.UNPACKING: 4,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.INIT_COUNTER: 3,
            CodePattern.TRY_EXCEPT_RERAISE: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.STRING_FORMAT: 9,
            CodePattern.GENERATOR_EXPRESSION: 7,
            CodePattern.LIST_COMPREHENSION: 7,
        }
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.LOOP_DICT_ITEMS: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 45,
            CodePattern.FUNCTION_TRANSFORMER: 21,
            CodePattern.GUARD_CLAUSE: 11,
            CodePattern.INIT_EMPTY_LIST: 9,
            CodePattern.IF_EMPTY_CHECK: 8,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.UNPACKING: 5,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.RETURN_LIST: 3,
            CodePattern.INIT_METHOD: 3,
            CodePattern.DICT_COMPREHENSION: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.INIT_EMPTY_DICT: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.UNPACKING): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 52,
            CodePattern.RETURN_COMPUTED: 40,
            CodePattern.UNPACKING: 32,
            CodePattern.INIT_DEFAULT_VALUE: 23,
            CodePattern.GUARD_CLAUSE: 22,
            CodePattern.IF_NOT_NONE: 17,
            CodePattern.IF_EMPTY_CHECK: 12,
            CodePattern.IF_TYPE_CHECK: 9,
            CodePattern.IF_NONE_CHECK: 8,
            CodePattern.TERNARY_EXPRESSION: 8,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.INIT_METHOD: 4,
            CodePattern.TRY_EXCEPT_PASS: 4,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.RETURN_DICT: 4,
            CodePattern.LOOP_FILTER: 3,
            CodePattern.EARLY_RETURN_SUCCESS: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.LOOP_FILTER): Counter(
        {CodePattern.IF_TYPE_CHECK: 3}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.TRY_EXCEPT_RERAISE: 6,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
        }
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 25,
            CodePattern.LOOP_ACCUMULATE: 11,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.RETURN_NONE: 4,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 8,
            CodePattern.LOOP_ACCUMULATE: 6,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.UNPACKING: 12,
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.GENERATOR_EXPRESSION: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 12,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.INIT_METHOD: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 35,
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.STRING_FORMAT: 11,
            CodePattern.INIT_METHOD: 10,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.FUNCTION_VALIDATOR: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 45,
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.INIT_DEFAULT_VALUE: 10,
            CodePattern.STRING_FORMAT: 9,
            CodePattern.GENERATOR_EXPRESSION: 5,
            CodePattern.PROPERTY_GETTER: 5,
            CodePattern.UNPACKING: 5,
            CodePattern.FUNCTION_VALIDATOR: 3,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.IF_NONE_CHECK: 5,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 65,
            CodePattern.RETURN_COMPUTED: 33,
            CodePattern.IF_TYPE_CHECK: 8,
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.TRY_EXCEPT_RERAISE: 7,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.CONTEXT_MANAGER: 5,
            CodePattern.PROPERTY_GETTER: 5,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.INIT_METHOD: 3,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 12,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 10,
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.GENERATOR_EXPRESSION: 4,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 6,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 64,
            CodePattern.RETURN_COMPUTED: 37,
            CodePattern.IF_EMPTY_CHECK: 11,
            CodePattern.FUNCTION_TRANSFORMER: 10,
            CodePattern.CONTEXT_MANAGER: 9,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.UNPACKING: 3,
            CodePattern.GUARD_CLAUSE: 3,
            CodePattern.INIT_COUNTER: 3,
            CodePattern.INIT_EMPTY_LIST: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 7,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.FUNCTION_TRANSFORMER: 5,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 44,
            CodePattern.IF_EMPTY_CHECK: 18,
            CodePattern.FUNCTION_TRANSFORMER: 16,
            CodePattern.UNPACKING: 9,
            CodePattern.GUARD_CLAUSE: 8,
            CodePattern.IF_NONE_CHECK: 8,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.IF_NOT_NONE: 6,
            CodePattern.INIT_EMPTY_LIST: 5,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.INIT_COUNTER: 3,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_NONE): Counter(
        {
            CodePattern.GUARD_CLAUSE: 23,
            CodePattern.RETURN_COMPUTED: 23,
            CodePattern.FUNCTION_TRANSFORMER: 21,
            CodePattern.IF_EMPTY_CHECK: 16,
            CodePattern.IF_TYPE_CHECK: 10,
            CodePattern.INIT_EMPTY_LIST: 8,
            CodePattern.UNPACKING: 7,
            CodePattern.TRY_EXCEPT_RERAISE: 7,
            CodePattern.LOGGING_CALL: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.TRY_FINALLY: 3,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.RETURN_NONE: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.INIT_EMPTY_DICT: 3,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.LOGGING_CALL: 5, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.LOGGING_CALL: 188,
            CodePattern.CONTEXT_MANAGER: 36,
            CodePattern.INIT_DEFAULT_VALUE: 25,
            CodePattern.DICT_GET_DEFAULT: 24,
            CodePattern.FUNCTION_TRANSFORMER: 16,
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.CLASS_METHOD: 4,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.TRY_FINALLY: 3,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.LOGGING_CALL, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.LOGGING_CALL: 8, CodePattern.LIST_COMPREHENSION: 4}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 102,
            CodePattern.CONTEXT_MANAGER: 44,
            CodePattern.FUNCTION_TRANSFORMER: 15,
            CodePattern.DICT_GET_DEFAULT: 14,
            CodePattern.INIT_DEFAULT_VALUE: 13,
            CodePattern.STRING_FORMAT: 12,
            CodePattern.TERNARY_EXPRESSION: 8,
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.LOOP_ENUMERATE: 6,
            CodePattern.CLASS_METHOD: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.LOOP_ZIP: 4,
            CodePattern.LOOP_DICT_ITEMS: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.LOGGING_CALL: 5, CodePattern.DICT_GET_DEFAULT: 4}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.LOGGING_CALL: 7,
            CodePattern.TRY_EXCEPT_LOG: 4,
            CodePattern.RETURN_LIST: 4,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.TERNARY_EXPRESSION: 6,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 55,
            CodePattern.INIT_DEFAULT_VALUE: 10,
            CodePattern.DICT_GET_DEFAULT: 8,
            CodePattern.LIST_COMPREHENSION: 6,
            CodePattern.LOGGING_CALL: 4,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 184,
            CodePattern.DICT_GET_DEFAULT: 168,
            CodePattern.INIT_DEFAULT_VALUE: 49,
            CodePattern.IF_EMPTY_CHECK: 19,
            CodePattern.CLASS_METHOD: 11,
            CodePattern.UNPACKING: 7,
            CodePattern.LIST_COMPREHENSION: 6,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.LOGGING_CALL: 6,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 164,
            CodePattern.CONTEXT_MANAGER: 140,
            CodePattern.LOGGING_CALL: 32,
            CodePattern.INIT_DEFAULT_VALUE: 22,
            CodePattern.LIST_COMPREHENSION: 9,
            CodePattern.UNPACKING: 5,
            CodePattern.CLASS_METHOD: 5,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 2997,
            CodePattern.INIT_DEFAULT_VALUE: 568,
            CodePattern.DICT_GET_DEFAULT: 165,
            CodePattern.FUNCTION_TRANSFORMER: 111,
            CodePattern.STRING_FORMAT: 98,
            CodePattern.UNPACKING: 82,
            CodePattern.LIST_COMPREHENSION: 70,
            CodePattern.LOGGING_CALL: 51,
            CodePattern.TRY_FINALLY: 47,
            CodePattern.CLASS_METHOD: 41,
            CodePattern.TERNARY_EXPRESSION: 30,
            CodePattern.GENERATOR_EXPRESSION: 28,
            CodePattern.INIT_EMPTY_LIST: 19,
            CodePattern.TRY_EXCEPT_PASS: 15,
            CodePattern.LOOP_DICT_ITEMS: 13,
            CodePattern.IF_EMPTY_CHECK: 12,
            CodePattern.INIT_METHOD: 10,
            CodePattern.LOOP_ACCUMULATE: 9,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.INIT_COUNTER: 5,
            CodePattern.LOOP_ENUMERATE: 4,
            CodePattern.LOOP_TRANSFORM: 4,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.LOOP_ZIP: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 1105,
            CodePattern.INIT_DEFAULT_VALUE: 170,
            CodePattern.FUNCTION_TRANSFORMER: 15,
            CodePattern.DICT_GET_DEFAULT: 14,
            CodePattern.UNPACKING: 13,
            CodePattern.STRING_FORMAT: 11,
            CodePattern.GENERATOR_EXPRESSION: 8,
            CodePattern.TRY_FINALLY: 6,
            CodePattern.CLASS_METHOD: 5,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.INIT_METHOD: 5,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 700,
            CodePattern.INIT_DEFAULT_VALUE: 628,
            CodePattern.DICT_GET_DEFAULT: 85,
            CodePattern.FUNCTION_TRANSFORMER: 60,
            CodePattern.UNPACKING: 32,
            CodePattern.STRING_FORMAT: 27,
            CodePattern.CLASS_METHOD: 20,
            CodePattern.LIST_COMPREHENSION: 19,
            CodePattern.TRY_FINALLY: 18,
            CodePattern.LOGGING_CALL: 18,
            CodePattern.TERNARY_EXPRESSION: 9,
            CodePattern.IF_EMPTY_CHECK: 8,
            CodePattern.LOOP_ZIP: 5,
            CodePattern.GENERATOR_EXPRESSION: 5,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.INIT_EMPTY_DICT: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 16,
            CodePattern.CONTEXT_MANAGER: 15,
            CodePattern.INIT_DEFAULT_VALUE: 15,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 376,
            CodePattern.CONTEXT_MANAGER: 47,
            CodePattern.INIT_DEFAULT_VALUE: 43,
            CodePattern.FUNCTION_TRANSFORMER: 34,
            CodePattern.RETURN_COMPUTED: 16,
            CodePattern.DICT_GET_DEFAULT: 15,
            CodePattern.STRING_FORMAT: 10,
            CodePattern.LOOP_ACCUMULATE: 9,
            CodePattern.LIST_COMPREHENSION: 8,
            CodePattern.IF_NOT_NONE: 8,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.LOGGING_CALL: 5,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.DICT_COMPREHENSION: 3,
            CodePattern.TRY_FINALLY: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 9,
            CodePattern.UNPACKING: 9,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 64,
            CodePattern.CONTEXT_MANAGER: 52,
            CodePattern.INIT_DEFAULT_VALUE: 15,
            CodePattern.DICT_GET_DEFAULT: 11,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.TRY_FINALLY: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 1901,
            CodePattern.CONTEXT_MANAGER: 203,
            CodePattern.FUNCTION_TRANSFORMER: 157,
            CodePattern.INIT_COUNTER: 123,
            CodePattern.INIT_METHOD: 88,
            CodePattern.DICT_GET_DEFAULT: 34,
            CodePattern.RETURN_COMPUTED: 27,
            CodePattern.LOGGING_CALL: 22,
            CodePattern.UNPACKING: 18,
            CodePattern.STRING_FORMAT: 15,
            CodePattern.CLASS_METHOD: 13,
            CodePattern.TRY_FINALLY: 8,
            CodePattern.LIST_COMPREHENSION: 8,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.PROPERTY_GETTER: 7,
            CodePattern.INIT_EMPTY_LIST: 7,
            CodePattern.STATIC_METHOD: 6,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.INIT_EMPTY_DICT: 6,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.LOOP_ACCUMULATE: 4,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.CONTEXT_MANAGER: 26, CodePattern.INIT_DEFAULT_VALUE: 8}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 55,
            CodePattern.CONTEXT_MANAGER: 24,
            CodePattern.FUNCTION_TRANSFORMER: 21,
            CodePattern.GUARD_CLAUSE: 9,
            CodePattern.UNPACKING: 7,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.RETURN_BOOL: 3,
            CodePattern.IF_NONE_CHECK: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 43,
            CodePattern.CONTEXT_MANAGER: 11,
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.INIT_DEFAULT_VALUE: 8,
            CodePattern.GENERATOR_EXPRESSION: 5,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 1620,
            CodePattern.INIT_DEFAULT_VALUE: 174,
            CodePattern.RETURN_COMPUTED: 125,
            CodePattern.CONTEXT_MANAGER: 108,
            CodePattern.STRING_FORMAT: 92,
            CodePattern.INIT_METHOD: 71,
            CodePattern.PROPERTY_GETTER: 64,
            CodePattern.GENERATOR_EXPRESSION: 63,
            CodePattern.DICT_GET_DEFAULT: 45,
            CodePattern.FUNCTION_VALIDATOR: 27,
            CodePattern.TERNARY_EXPRESSION: 26,
            CodePattern.LOGGING_CALL: 25,
            CodePattern.LIST_COMPREHENSION: 24,
            CodePattern.GUARD_CLAUSE: 24,
            CodePattern.UNPACKING: 23,
            CodePattern.INIT_COUNTER: 21,
            CodePattern.CLASS_METHOD: 19,
            CodePattern.IF_EMPTY_CHECK: 16,
            CodePattern.IF_NONE_CHECK: 13,
            CodePattern.RETURN_NONE: 10,
            CodePattern.INIT_EMPTY_LIST: 8,
            CodePattern.STATIC_METHOD: 8,
            CodePattern.LOOP_ACCUMULATE: 7,
            CodePattern.IF_TYPE_CHECK: 7,
            CodePattern.TRY_FINALLY: 5,
            CodePattern.TRY_EXCEPT_PASS: 5,
            CodePattern.RETURN_BOOL: 5,
            CodePattern.LOOP_DICT_ITEMS: 4,
            CodePattern.INIT_EMPTY_DICT: 3,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 62,
            CodePattern.GENERATOR_EXPRESSION: 48,
            CodePattern.STRING_FORMAT: 25,
            CodePattern.INIT_METHOD: 15,
            CodePattern.RETURN_COMPUTED: 15,
            CodePattern.LIST_COMPREHENSION: 9,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.PROPERTY_GETTER: 4,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_COUNTER): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 102,
            CodePattern.INIT_COUNTER: 59,
            CodePattern.FUNCTION_TRANSFORMER: 19,
            CodePattern.INIT_METHOD: 15,
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.INIT_EMPTY_LIST: 5,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.INIT_EMPTY_DICT: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.PROPERTY_GETTER: 3,
        }
    ),
    (CodePattern.INIT_COUNTER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 94,
            CodePattern.INIT_COUNTER: 47,
            CodePattern.INIT_METHOD: 17,
            CodePattern.FUNCTION_TRANSFORMER: 14,
            CodePattern.CONTEXT_MANAGER: 5,
            CodePattern.CLASS_METHOD: 3,
            CodePattern.PROPERTY_GETTER: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.INIT_EMPTY_LIST: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 25,
            CodePattern.CONTEXT_MANAGER: 8,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 109,
            CodePattern.DICT_GET_DEFAULT: 40,
            CodePattern.INIT_DEFAULT_VALUE: 26,
            CodePattern.FUNCTION_TRANSFORMER: 4,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.CLASS_METHOD): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 25,
            CodePattern.INIT_DEFAULT_VALUE: 11,
            CodePattern.CLASS_METHOD: 9,
            CodePattern.DICT_GET_DEFAULT: 7,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.LOGGING_CALL: 5,
            CodePattern.LIST_COMPREHENSION: 4,
        }
    ),
    (CodePattern.STATIC_METHOD, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.CLASS_METHOD: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 393,
            CodePattern.RETURN_COMPUTED: 190,
            CodePattern.INIT_METHOD: 36,
            CodePattern.INIT_DEFAULT_VALUE: 34,
            CodePattern.GENERATOR_EXPRESSION: 23,
            CodePattern.PROPERTY_GETTER: 22,
            CodePattern.GUARD_CLAUSE: 19,
            CodePattern.FUNCTION_VALIDATOR: 17,
            CodePattern.IF_EMPTY_CHECK: 17,
            CodePattern.CONTEXT_MANAGER: 15,
            CodePattern.STRING_FORMAT: 15,
            CodePattern.IF_TYPE_CHECK: 15,
            CodePattern.TERNARY_EXPRESSION: 12,
            CodePattern.LIST_COMPREHENSION: 10,
            CodePattern.INIT_COUNTER: 9,
            CodePattern.TRY_FINALLY: 6,
            CodePattern.IF_NOT_NONE: 5,
            CodePattern.CLASS_METHOD: 5,
            CodePattern.IF_NONE_CHECK: 5,
            CodePattern.LOOP_DICT_ITEMS: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.DICT_COMPREHENSION: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.RETURN_BOOL: 3,
            CodePattern.LOGGING_CALL: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 85,
            CodePattern.UNPACKING: 37,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.DICT_GET_DEFAULT: 7,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.TRY_FINALLY: 5,
            CodePattern.CLASS_METHOD: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.UNPACKING): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 12,
            CodePattern.FUNCTION_TRANSFORMER: 8,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.UNPACKING: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 31,
            CodePattern.INIT_DEFAULT_VALUE: 31,
            CodePattern.FUNCTION_TRANSFORMER: 17,
            CodePattern.UNPACKING: 14,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.LOOP_ENUMERATE, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.UNPACKING): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 84,
            CodePattern.UNPACKING: 51,
            CodePattern.INIT_DEFAULT_VALUE: 22,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 11,
            CodePattern.LOOP_ACCUMULATE: 10,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.LOOP_ZIP: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 9,
            CodePattern.LOOP_ACCUMULATE: 7,
            CodePattern.INIT_DEFAULT_VALUE: 4,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.LIST_COMPREHENSION: 11, CodePattern.CONTEXT_MANAGER: 4}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 79,
            CodePattern.LIST_COMPREHENSION: 56,
            CodePattern.INIT_DEFAULT_VALUE: 12,
            CodePattern.FUNCTION_TRANSFORMER: 12,
            CodePattern.GENERATOR_EXPRESSION: 7,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 16,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.LIST_COMPREHENSION: 6,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 98,
            CodePattern.RETURN_COMPUTED: 47,
            CodePattern.INIT_DEFAULT_VALUE: 27,
            CodePattern.CONTEXT_MANAGER: 18,
            CodePattern.INIT_METHOD: 15,
            CodePattern.GUARD_CLAUSE: 7,
            CodePattern.DICT_GET_DEFAULT: 5,
            CodePattern.UNPACKING: 5,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.INIT_COUNTER: 4,
            CodePattern.RETURN_LIST: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.RETURN_DICT: 3,
            CodePattern.RETURN_NONE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.PROPERTY_GETTER: 3,
            CodePattern.RETURN_BOOL: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 20,
            CodePattern.LIST_COMPREHENSION: 9,
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.INIT_DEFAULT_VALUE: 4,
        }
    ),
    (CodePattern.TRY_FINALLY, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.CONTEXT_MANAGER: 12}
    ),
    (CodePattern.CLASS_METHOD, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 12, CodePattern.FUNCTION_TRANSFORMER: 9}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 135,
            CodePattern.FUNCTION_TRANSFORMER: 70,
            CodePattern.CONTEXT_MANAGER: 43,
            CodePattern.INIT_METHOD: 43,
            CodePattern.INIT_COUNTER: 13,
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.UNPACKING: 3,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.CLASS_METHOD): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 11,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 1001,
            CodePattern.CONTEXT_MANAGER: 153,
            CodePattern.INIT_DEFAULT_VALUE: 83,
            CodePattern.LOGGING_CALL: 61,
            CodePattern.CLASS_METHOD: 29,
            CodePattern.FUNCTION_TRANSFORMER: 22,
            CodePattern.UNPACKING: 21,
            CodePattern.LIST_COMPREHENSION: 15,
            CodePattern.INIT_EMPTY_LIST: 7,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.LOOP_DICT_ITEMS: 3,
            CodePattern.TRY_FINALLY: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.CONTEXT_MANAGER: 9}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 40,
            CodePattern.STRING_FORMAT: 10,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.CLASS_METHOD): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.CLASS_METHOD: 7,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 6}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.CONTEXT_MANAGER: 4, CodePattern.LIST_COMPREHENSION: 3}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.TRY_FINALLY): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 49,
            CodePattern.TRY_FINALLY: 10,
            CodePattern.DICT_GET_DEFAULT: 7,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.INIT_DEFAULT_VALUE: 6,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.CLASS_METHOD): Counter(
        {
            CodePattern.LOGGING_CALL: 28,
            CodePattern.DICT_GET_DEFAULT: 7,
            CodePattern.CONTEXT_MANAGER: 5,
            CodePattern.LIST_COMPREHENSION: 4,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 71,
            CodePattern.FUNCTION_TRANSFORMER: 28,
            CodePattern.INIT_DEFAULT_VALUE: 21,
            CodePattern.LOGGING_CALL: 11,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.UNPACKING: 5,
            CodePattern.DICT_GET_DEFAULT: 5,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.INIT_EMPTY_LIST: 4, CodePattern.LOGGING_CALL: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.LOOP_FILTER: 18,
            CodePattern.INIT_EMPTY_LIST: 15,
            CodePattern.LOOP_TRANSFORM: 12,
            CodePattern.INIT_DEFAULT_VALUE: 8,
            CodePattern.UNPACKING: 4,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_TRANSFORM): Counter(
        {
            CodePattern.RETURN_COMPUTED: 14,
            CodePattern.UNPACKING: 12,
            CodePattern.STRING_FORMAT: 9,
            CodePattern.CONTEXT_MANAGER: 5,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.LOOP_TRANSFORM): Counter(
        {CodePattern.LOOP_TRANSFORM: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.CLASS_METHOD, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.CONTEXT_MANAGER: 7, CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 402,
            CodePattern.FUNCTION_TRANSFORMER: 190,
            CodePattern.GUARD_CLAUSE: 42,
            CodePattern.IF_EMPTY_CHECK: 37,
            CodePattern.INIT_DEFAULT_VALUE: 31,
            CodePattern.CONTEXT_MANAGER: 30,
            CodePattern.IF_NONE_CHECK: 28,
            CodePattern.RETURN_LIST: 27,
            CodePattern.RETURN_BOOL: 21,
            CodePattern.TERNARY_EXPRESSION: 16,
            CodePattern.IF_TYPE_CHECK: 13,
            CodePattern.RETURN_NONE: 12,
            CodePattern.UNPACKING: 11,
            CodePattern.EARLY_RETURN_SUCCESS: 10,
            CodePattern.IF_NOT_NONE: 10,
            CodePattern.DICT_GET_DEFAULT: 9,
            CodePattern.INIT_METHOD: 6,
            CodePattern.LOOP_ACCUMULATE: 6,
            CodePattern.INIT_EMPTY_DICT: 5,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.RETURN_DICT: 4,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.TRY_EXCEPT_PASS: 4,
            CodePattern.TRY_EXCEPT_RERAISE: 4,
            CodePattern.LOOP_DICT_ITEMS: 3,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.INIT_COUNTER: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.DICT_GET_DEFAULT): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 12,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 16,
            CodePattern.INIT_DEFAULT_VALUE: 9,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.LOGGING_CALL: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.CONTEXT_MANAGER: 14}
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.STRING_FORMAT: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.IF_TYPE_CHECK: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 27,
            CodePattern.INIT_DEFAULT_VALUE: 14,
            CodePattern.LOOP_DICT_ITEMS: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 39,
            CodePattern.TERNARY_EXPRESSION: 11,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 29,
            CodePattern.TERNARY_EXPRESSION: 11,
            CodePattern.DICT_GET_DEFAULT: 8,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.LIST_COMPREHENSION: 4,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.INIT_METHOD: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 14,
            CodePattern.INIT_METHOD: 10,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_ZIP): Counter(
        {CodePattern.CONTEXT_MANAGER: 6, CodePattern.LOOP_ZIP: 5}
    ),
    (CodePattern.LOOP_ZIP, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.LOOP_ACCUMULATE: 4,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 8,
            CodePattern.LOOP_FILTER: 6,
            CodePattern.LOOP_TRANSFORM: 5,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.LOOP_ENUMERATE: 3,
        }
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 37,
            CodePattern.RETURN_COMPUTED: 14,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 11, CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_EMPTY_DICT): Counter(
        {CodePattern.LOOP_FILTER: 5, CodePattern.INIT_EMPTY_LIST: 3}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.INIT_EMPTY_LIST: 5, CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.GENERATOR_EXPRESSION: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.GENERATOR_EXPRESSION: 21,
            CodePattern.CONTEXT_MANAGER: 12,
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.GENERATOR_EXPRESSION: 3}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.TRY_EXCEPT_PASS): Counter(
        {CodePattern.CONTEXT_MANAGER: 14}
    ),
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 17}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 54,
            CodePattern.INIT_DEFAULT_VALUE: 15,
            CodePattern.TRY_FINALLY: 8,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.UNPACKING: 4,
            CodePattern.LOGGING_CALL: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 74,
            CodePattern.DICT_GET_DEFAULT: 44,
            CodePattern.LOGGING_CALL: 43,
            CodePattern.FUNCTION_TRANSFORMER: 15,
            CodePattern.INIT_DEFAULT_VALUE: 14,
            CodePattern.LIST_COMPREHENSION: 6,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.LOGGING_CALL, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 5}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.STRING_FORMAT: 14,
            CodePattern.CONTEXT_MANAGER: 9,
            CodePattern.GENERATOR_EXPRESSION: 6,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.UNPACKING: 4,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 5, CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.INIT_EMPTY_LIST: 5}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.TRY_FINALLY: 7}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 36,
            CodePattern.INIT_DEFAULT_VALUE: 20,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.INIT_COUNTER: 5,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 36,
            CodePattern.STRING_FORMAT: 31,
            CodePattern.RETURN_COMPUTED: 19,
            CodePattern.CONTEXT_MANAGER: 13,
            CodePattern.LIST_COMPREHENSION: 11,
            CodePattern.INIT_DEFAULT_VALUE: 8,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.INIT_METHOD: 6,
            CodePattern.LOGGING_CALL: 6,
            CodePattern.RETURN_DICT: 3,
            CodePattern.CLASS_METHOD: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.PROPERTY_GETTER: 3,
        }
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 99,
            CodePattern.UNPACKING: 27,
            CodePattern.FUNCTION_TRANSFORMER: 26,
            CodePattern.GUARD_CLAUSE: 19,
            CodePattern.IF_EMPTY_CHECK: 18,
            CodePattern.RETURN_LIST: 14,
            CodePattern.IF_NONE_CHECK: 12,
            CodePattern.IF_TYPE_CHECK: 9,
            CodePattern.INIT_EMPTY_LIST: 9,
            CodePattern.LOOP_ACCUMULATE: 8,
            CodePattern.LIST_COMPREHENSION: 8,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.INIT_METHOD: 7,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.RETURN_BOOL: 6,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.INIT_EMPTY_DICT: 4,
            CodePattern.TRY_EXCEPT_RERAISE: 4,
            CodePattern.RETURN_NONE: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.TRY_FINALLY, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.TRY_FINALLY: 3,
        }
    ),
    (CodePattern.TRY_FINALLY, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.LOOP_FILTER: 53,
            CodePattern.RETURN_COMPUTED: 24,
            CodePattern.INIT_EMPTY_LIST: 19,
            CodePattern.LOOP_TRANSFORM: 16,
            CodePattern.FUNCTION_TRANSFORMER: 11,
            CodePattern.IF_EMPTY_CHECK: 10,
            CodePattern.IF_NOT_NONE: 9,
            CodePattern.LOGGING_CALL: 8,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.LOOP_ENUMERATE: 6,
            CodePattern.IF_NONE_CHECK: 5,
            CodePattern.LOOP_DICT_ITEMS: 4,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.UNPACKING: 4,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.INIT_EMPTY_DICT: 4,
            CodePattern.TRY_EXCEPT_PASS: 4,
            CodePattern.INIT_COUNTER: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 15,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.CONTEXT_MANAGER: 5, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.TRY_FINALLY): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 10,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.TRY_FINALLY: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.TERNARY_EXPRESSION: 55,
            CodePattern.FUNCTION_TRANSFORMER: 24,
            CodePattern.CONTEXT_MANAGER: 11,
            CodePattern.RETURN_COMPUTED: 11,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 13,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.INIT_EMPTY_LIST: 5,
            CodePattern.INIT_COUNTER: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.LOOP_FILTER: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.STATIC_METHOD): Counter(
        {CodePattern.RETURN_BOOL: 4}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 58,
            CodePattern.INIT_DEFAULT_VALUE: 22,
            CodePattern.CONTEXT_MANAGER: 12,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.LOGGING_CALL: 5,
        }
    ),
    (CodePattern.LOGGING_CALL, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.LOGGING_CALL: 73,
            CodePattern.CONTEXT_MANAGER: 31,
            CodePattern.DICT_GET_DEFAULT: 10,
            CodePattern.INIT_DEFAULT_VALUE: 7,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.STRING_FORMAT: 12,
            CodePattern.FUNCTION_TRANSFORMER: 11,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.INIT_COUNTER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 21,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.RETURN_LIST: 4,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.EARLY_RETURN_SUCCESS: 3,
            CodePattern.IF_NONE_CHECK: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_LIST): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 90,
            CodePattern.INIT_DEFAULT_VALUE: 18,
            CodePattern.LOGGING_CALL: 10,
            CodePattern.UNPACKING: 9,
            CodePattern.CONTEXT_MANAGER: 8,
            CodePattern.RETURN_LIST: 5,
            CodePattern.FUNCTION_VALIDATOR: 5,
        }
    ),
    (CodePattern.RETURN_LIST, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.CONTEXT_MANAGER: 5,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.TRY_FINALLY, CodePattern.TRY_FINALLY): Counter(
        {
            CodePattern.TRY_FINALLY: 10,
            CodePattern.CONTEXT_MANAGER: 10,
            CodePattern.INIT_DEFAULT_VALUE: 5,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_BOOL): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 51,
            CodePattern.INIT_DEFAULT_VALUE: 12,
            CodePattern.RETURN_BOOL: 8,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.CLASS_METHOD: 3,
            CodePattern.LOGGING_CALL: 3,
        }
    ),
    (CodePattern.RETURN_BOOL, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 46,
            CodePattern.FUNCTION_TRANSFORMER: 17,
            CodePattern.TERNARY_EXPRESSION: 17,
            CodePattern.GUARD_CLAUSE: 17,
            CodePattern.IF_NONE_CHECK: 10,
            CodePattern.INIT_EMPTY_LIST: 8,
            CodePattern.IF_EMPTY_CHECK: 8,
            CodePattern.UNPACKING: 6,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.INIT_METHOD: 4,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.RETURN_DICT: 3,
            CodePattern.EARLY_RETURN_SUCCESS: 3,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.LOOP_DICT_ITEMS): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.STATIC_METHOD, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.RETURN_BOOL: 5}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_BOOL): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 44,
            CodePattern.RETURN_BOOL: 10,
            CodePattern.STATIC_METHOD: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.STATIC_METHOD, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 3}
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 16, CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.STATIC_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 8, CodePattern.INIT_EMPTY_LIST: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_FILTER): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 39,
            CodePattern.RETURN_COMPUTED: 25,
            CodePattern.IF_TYPE_CHECK: 15,
            CodePattern.LOOP_FILTER: 14,
            CodePattern.UNPACKING: 10,
            CodePattern.IF_NONE_CHECK: 9,
            CodePattern.INIT_EMPTY_LIST: 8,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.TERNARY_EXPRESSION: 8,
            CodePattern.LOOP_ACCUMULATE: 8,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.LOGGING_CALL: 5,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.LOOP_DICT_ITEMS: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.LOOP_FILTER, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 9}
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 4}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 48,
            CodePattern.STRING_FORMAT: 14,
            CodePattern.RETURN_COMPUTED: 11,
            CodePattern.INIT_METHOD: 5,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.INIT_COUNTER, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 4, CodePattern.LOOP_ACCUMULATE: 4}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.STATIC_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 87,
            CodePattern.LIST_COMPREHENSION: 14,
            CodePattern.IF_TYPE_CHECK: 12,
            CodePattern.IF_EMPTY_CHECK: 8,
            CodePattern.INIT_EMPTY_LIST: 6,
            CodePattern.GUARD_CLAUSE: 5,
            CodePattern.UNPACKING: 5,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.RETURN_LIST: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
        }
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.IF_TYPE_CHECK: 83,
            CodePattern.RETURN_COMPUTED: 73,
            CodePattern.FUNCTION_TRANSFORMER: 53,
            CodePattern.GUARD_CLAUSE: 8,
            CodePattern.GENERATOR_EXPRESSION: 7,
            CodePattern.TRY_EXCEPT_RERAISE: 6,
            CodePattern.INIT_METHOD: 5,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.FUNCTION_VALIDATOR: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 5}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 23,
            CodePattern.RETURN_COMPUTED: 15,
            CodePattern.IF_EMPTY_CHECK: 4,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 74,
            CodePattern.IF_EMPTY_CHECK: 26,
            CodePattern.INIT_DEFAULT_VALUE: 18,
            CodePattern.TERNARY_EXPRESSION: 15,
            CodePattern.IF_NONE_CHECK: 15,
            CodePattern.RETURN_COMPUTED: 11,
            CodePattern.IF_NOT_NONE: 10,
            CodePattern.IF_TYPE_CHECK: 6,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.INIT_METHOD: 4,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.DICT_COMPREHENSION: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.CLASS_METHOD): Counter(
        {
            CodePattern.RETURN_COMPUTED: 16,
            CodePattern.CLASS_METHOD: 13,
            CodePattern.INIT_EMPTY_LIST: 12,
            CodePattern.IF_EMPTY_CHECK: 9,
            CodePattern.GUARD_CLAUSE: 5,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.INIT_EMPTY_DICT: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.LOOP_FILTER, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.UNPACKING: 6,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 13,
            CodePattern.LIST_COMPREHENSION: 9,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.LOGGING_CALL: 4,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 7, CodePattern.INIT_EMPTY_LIST: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_LIST: 28,
            CodePattern.GUARD_CLAUSE: 25,
            CodePattern.RETURN_COMPUTED: 23,
            CodePattern.IF_EMPTY_CHECK: 23,
            CodePattern.INIT_EMPTY_LIST: 13,
            CodePattern.IF_NONE_CHECK: 11,
            CodePattern.FUNCTION_TRANSFORMER: 10,
            CodePattern.UNPACKING: 9,
            CodePattern.EARLY_RETURN_SUCCESS: 6,
            CodePattern.LIST_COMPREHENSION: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.DICT_COMPREHENSION: 5,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.RETURN_DICT: 3,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_TRANSFORM): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 21,
            CodePattern.DICT_GET_DEFAULT: 19,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.GUARD_CLAUSE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_EMPTY_DICT): Counter(
        {CodePattern.CONTEXT_MANAGER: 4}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 81,
            CodePattern.RETURN_COMPUTED: 33,
            CodePattern.IF_NOT_NONE: 15,
            CodePattern.IF_NONE_CHECK: 15,
            CodePattern.IF_EMPTY_CHECK: 11,
            CodePattern.INIT_METHOD: 10,
            CodePattern.PROPERTY_GETTER: 9,
            CodePattern.UNPACKING: 8,
            CodePattern.IF_TYPE_CHECK: 8,
            CodePattern.GUARD_CLAUSE: 5,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.LOOP_DICT_ITEMS: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 170,
            CodePattern.FUNCTION_TRANSFORMER: 38,
            CodePattern.IF_EMPTY_CHECK: 28,
            CodePattern.UNPACKING: 25,
            CodePattern.INIT_DEFAULT_VALUE: 16,
            CodePattern.GUARD_CLAUSE: 14,
            CodePattern.RETURN_LIST: 13,
            CodePattern.IF_TYPE_CHECK: 13,
            CodePattern.INIT_EMPTY_LIST: 11,
            CodePattern.TRY_EXCEPT_RERAISE: 8,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.DICT_GET_DEFAULT: 7,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.IF_NOT_NONE: 5,
            CodePattern.RETURN_DICT: 4,
            CodePattern.RETURN_NONE: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.RETURN_BOOL: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 13,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.RETURN_NONE: 4,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.RETURN_COMPUTED: 76,
            CodePattern.FUNCTION_TRANSFORMER: 16,
            CodePattern.INIT_METHOD: 6,
            CodePattern.RETURN_NONE: 5,
            CodePattern.RETURN_LIST: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 21,
            CodePattern.GENERATOR_EXPRESSION: 9,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.CONTEXT_MANAGER: 6}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_NONE): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 41,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.INIT_METHOD: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 8, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 49,
            CodePattern.FUNCTION_TRANSFORMER: 38,
            CodePattern.CONTEXT_MANAGER: 34,
            CodePattern.RETURN_COMPUTED: 19,
            CodePattern.INIT_METHOD: 8,
            CodePattern.INIT_COUNTER: 7,
            CodePattern.LOOP_ACCUMULATE: 7,
            CodePattern.INIT_EMPTY_LIST: 6,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.STRING_FORMAT: 6,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_DICT): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 57,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.TERNARY_EXPRESSION: 4,
        }
    ),
    (CodePattern.RETURN_DICT, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3, CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.RETURN_NONE, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 52,
            CodePattern.RETURN_COMPUTED: 11,
            CodePattern.INIT_DEFAULT_VALUE: 9,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.INIT_METHOD: 6,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.CLASS_METHOD: 3,
            CodePattern.TRY_EXCEPT_PASS: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_EMPTY_DICT): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 9, CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 26,
            CodePattern.LOGGING_CALL: 23,
            CodePattern.CONTEXT_MANAGER: 20,
            CodePattern.DICT_GET_DEFAULT: 8,
            CodePattern.FUNCTION_TRANSFORMER: 4,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 11,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.LOGGING_CALL: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 8,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.STRING_FORMAT: 23,
            CodePattern.UNPACKING: 17,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.UNPACKING): Counter(
        {
            CodePattern.STRING_FORMAT: 29,
            CodePattern.UNPACKING: 12,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 8}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 9,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.LOOP_TRANSFORM: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.UNPACKING: 8,
            CodePattern.LOOP_TRANSFORM: 4,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.LOOP_FILTER: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_ENUMERATE): Counter(
        {CodePattern.CONTEXT_MANAGER: 5}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 9,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.TRY_EXCEPT_PASS: 3,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.RETURN_NONE: 7,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.INIT_EMPTY_DICT: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.GENERATOR_EXPRESSION: 12,
            CodePattern.FUNCTION_TRANSFORMER: 10,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 37,
            CodePattern.FUNCTION_TRANSFORMER: 26,
            CodePattern.UNPACKING: 23,
            CodePattern.GUARD_CLAUSE: 16,
            CodePattern.INIT_EMPTY_LIST: 7,
            CodePattern.IF_NONE_CHECK: 7,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.RETURN_LIST: 4,
            CodePattern.RETURN_BOOL: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.FUNCTION_VALIDATOR: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 26,
            CodePattern.RETURN_NONE: 16,
            CodePattern.IF_EMPTY_CHECK: 14,
            CodePattern.GUARD_CLAUSE: 12,
            CodePattern.FUNCTION_TRANSFORMER: 9,
            CodePattern.IF_NONE_CHECK: 7,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.UNPACKING: 3,
            CodePattern.RETURN_BOOL: 3,
            CodePattern.RETURN_LIST: 3,
            CodePattern.INIT_EMPTY_LIST: 3,
        }
    ),
    (CodePattern.LOGGING_CALL, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 39,
            CodePattern.FUNCTION_TRANSFORMER: 12,
            CodePattern.GUARD_CLAUSE: 8,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.RETURN_DICT: 3,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 20,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.INIT_EMPTY_DICT): Counter(
        {
            CodePattern.LOOP_DICT_ITEMS: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.LOGGING_CALL: 20,
            CodePattern.INIT_DEFAULT_VALUE: 17,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.LOGGING_CALL, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.LOGGING_CALL: 7}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 17,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.LOOP_FILTER: 3,
            CodePattern.INIT_COUNTER: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.RETURN_DICT: 4}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.DICT_COMPREHENSION): Counter(
        {CodePattern.CONTEXT_MANAGER: 4, CodePattern.DICT_GET_DEFAULT: 4}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.IF_TYPE_CHECK: 5, CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 9, CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 78,
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.FUNCTION_VALIDATOR: 5,
            CodePattern.PROPERTY_GETTER: 5,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.INIT_COUNTER: 4,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.DICT_COMPREHENSION: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.GENERATOR_EXPRESSION: 7,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.LIST_COMPREHENSION: 4,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_NONE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 20,
            CodePattern.IF_EMPTY_CHECK: 12,
            CodePattern.GUARD_CLAUSE: 11,
            CodePattern.FUNCTION_TRANSFORMER: 9,
            CodePattern.UNPACKING: 8,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.LIST_COMPREHENSION: 6,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.LOGGING_CALL: 5,
            CodePattern.IF_NONE_CHECK: 5,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.INIT_COUNTER: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 8, CodePattern.LIST_COMPREHENSION: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 12,
            CodePattern.CONTEXT_MANAGER: 11,
            CodePattern.INIT_COUNTER: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 12,
            CodePattern.CONTEXT_MANAGER: 11,
            CodePattern.DICT_GET_DEFAULT: 5,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.DICT_GET_DEFAULT: 4}
    ),
    (CodePattern.INIT_METHOD, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 11,
            CodePattern.TERNARY_EXPRESSION: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_COUNTER): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 9,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.INIT_COUNTER: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 15,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.LIST_COMPREHENSION: 4}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.INIT_COUNTER: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 7}
    ),
    (CodePattern.INIT_METHOD, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 34,
            CodePattern.RETURN_COMPUTED: 18,
            CodePattern.INIT_METHOD: 7,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.PROPERTY_GETTER: 5,
            CodePattern.TRY_EXCEPT_RERAISE: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 102,
            CodePattern.IF_TYPE_CHECK: 7,
            CodePattern.LOOP_ACCUMULATE: 6,
            CodePattern.UNPACKING: 5,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_NONE: 9,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 67,
            CodePattern.FUNCTION_VALIDATOR: 5,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_VALIDATOR): Counter(
        {
            CodePattern.GUARD_CLAUSE: 48,
            CodePattern.IF_EMPTY_CHECK: 21,
            CodePattern.IF_NONE_CHECK: 11,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_NONE: 17,
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.RETURN_BOOL: 6,
            CodePattern.RETURN_LIST: 5,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_NONE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 43,
            CodePattern.GUARD_CLAUSE: 8,
            CodePattern.UNPACKING: 7,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.IF_TYPE_CHECK: 6,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.TRY_EXCEPT_PASS: 4,
            CodePattern.TRY_EXCEPT_RERAISE: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.RETURN_BOOL, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 29,
            CodePattern.RETURN_BOOL: 22,
            CodePattern.GUARD_CLAUSE: 15,
            CodePattern.FUNCTION_TRANSFORMER: 13,
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.CONTEXT_MANAGER: 5,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.RETURN_BOOL, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.INIT_DEFAULT_VALUE: 4,
        }
    ),
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 24,
            CodePattern.GENERATOR_EXPRESSION: 7,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.INIT_METHOD: 4,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_EMPTY_DICT): Counter(
        {
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.LOOP_DICT_ITEMS: 7,
            CodePattern.IF_NOT_NONE: 6,
            CodePattern.INIT_EMPTY_DICT: 6,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.LOOP_FILTER: 4,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.TRY_EXCEPT_PASS: 3,
            CodePattern.DICT_COMPREHENSION: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.INIT_EMPTY_DICT): Counter(
        {
            CodePattern.INIT_EMPTY_DICT: 9,
            CodePattern.LOOP_DICT_ITEMS: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.PROPERTY_GETTER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 152,
            CodePattern.PROPERTY_GETTER: 20,
            CodePattern.GUARD_CLAUSE: 20,
            CodePattern.IF_EMPTY_CHECK: 17,
            CodePattern.FUNCTION_TRANSFORMER: 16,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.UNPACKING: 6,
            CodePattern.EARLY_RETURN_SUCCESS: 5,
            CodePattern.INIT_METHOD: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.IF_NONE_CHECK: 3,
        }
    ),
    (CodePattern.RETURN_DICT, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 25,
            CodePattern.RETURN_DICT: 25,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.GUARD_CLAUSE: 3,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.RETURN_COMPUTED: 6}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.INIT_EMPTY_LIST: 4}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.DICT_GET_DEFAULT): Counter(
        {CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 16, CodePattern.RETURN_NONE: 4}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.RETURN_COMPUTED: 205,
            CodePattern.GUARD_CLAUSE: 93,
            CodePattern.FUNCTION_TRANSFORMER: 92,
            CodePattern.STRING_FORMAT: 22,
            CodePattern.IF_EMPTY_CHECK: 22,
            CodePattern.RETURN_NONE: 21,
            CodePattern.INIT_DEFAULT_VALUE: 15,
            CodePattern.EARLY_RETURN_SUCCESS: 15,
            CodePattern.PROPERTY_GETTER: 13,
            CodePattern.INIT_METHOD: 12,
            CodePattern.IF_TYPE_CHECK: 11,
            CodePattern.CONTEXT_MANAGER: 10,
            CodePattern.RETURN_BOOL: 10,
            CodePattern.UNPACKING: 9,
            CodePattern.DICT_GET_DEFAULT: 8,
            CodePattern.LIST_COMPREHENSION: 8,
            CodePattern.IF_NONE_CHECK: 7,
            CodePattern.LOOP_ACCUMULATE: 7,
            CodePattern.RETURN_LIST: 6,
            CodePattern.INIT_EMPTY_LIST: 6,
            CodePattern.TERNARY_EXPRESSION: 6,
            CodePattern.LOGGING_CALL: 5,
            CodePattern.TRY_EXCEPT_PASS: 5,
            CodePattern.TRY_EXCEPT_RERAISE: 5,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 6, CodePattern.INIT_EMPTY_LIST: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 224,
            CodePattern.RETURN_NONE: 76,
            CodePattern.RETURN_LIST: 58,
            CodePattern.RETURN_BOOL: 39,
            CodePattern.GUARD_CLAUSE: 18,
            CodePattern.FUNCTION_TRANSFORMER: 17,
            CodePattern.UNPACKING: 11,
            CodePattern.RETURN_DICT: 8,
            CodePattern.INIT_DEFAULT_VALUE: 8,
            CodePattern.GENERATOR_EXPRESSION: 6,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.EARLY_RETURN_SUCCESS: 4,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.LOOP_DICT_ITEMS: 3,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_BOOL): Counter(
        {
            CodePattern.RETURN_BOOL: 38,
            CodePattern.GUARD_CLAUSE: 33,
            CodePattern.RETURN_COMPUTED: 26,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.EARLY_RETURN_SUCCESS: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.RETURN_COMPUTED: 30,
            CodePattern.GUARD_CLAUSE: 12,
            CodePattern.DICT_GET_DEFAULT: 11,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.IF_NOT_NONE: 6,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 29, CodePattern.INIT_DEFAULT_VALUE: 5}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.FUNCTION_VALIDATOR): Counter(
        {
            CodePattern.GUARD_CLAUSE: 8,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.IF_EMPTY_CHECK: 4,
        }
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 29,
            CodePattern.RETURN_NONE: 19,
            CodePattern.GUARD_CLAUSE: 17,
            CodePattern.RETURN_BOOL: 16,
            CodePattern.RETURN_LIST: 7,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.GUARD_CLAUSE: 32,
            CodePattern.RETURN_COMPUTED: 20,
            CodePattern.FUNCTION_TRANSFORMER: 11,
            CodePattern.EARLY_RETURN_SUCCESS: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.GUARD_CLAUSE: 7,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.UNPACKING: 7,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.IF_NONE_CHECK: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.INIT_COUNTER: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 94,
            CodePattern.LOGGING_CALL: 75,
            CodePattern.CONTEXT_MANAGER: 22,
            CodePattern.INIT_DEFAULT_VALUE: 8,
            CodePattern.CLASS_METHOD: 7,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.STRING_FORMAT: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.CONTEXT_MANAGER: 5}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 14,
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.GUARD_CLAUSE: 5,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.UNPACKING): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 14, CodePattern.UNPACKING: 5}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 15,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.UNPACKING: 5,
            CodePattern.PROPERTY_GETTER: 4,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.UNPACKING: 5,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.IF_NONE_CHECK: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.DICT_GET_DEFAULT): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 7,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.GENERATOR_EXPRESSION: 5,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 30,
            CodePattern.LOGGING_CALL: 8,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.CLASS_METHOD: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 11}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 27,
            CodePattern.PROPERTY_GETTER: 7,
            CodePattern.LOGGING_CALL: 6,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 36,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 4, CodePattern.RETURN_BOOL: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.RETURN_LIST: 55,
            CodePattern.GUARD_CLAUSE: 10,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.EARLY_RETURN_SUCCESS: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.DICT_GET_DEFAULT): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 23,
            CodePattern.UNPACKING: 16,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6, CodePattern.UNPACKING: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 55,
            CodePattern.RETURN_COMPUTED: 42,
            CodePattern.INIT_DEFAULT_VALUE: 8,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.DICT_COMPREHENSION: 5,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.RETURN_DICT: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.UNPACKING): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 7,
            CodePattern.UNPACKING: 4,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_ENUMERATE): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 8}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 51,
            CodePattern.RETURN_COMPUTED: 19,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.INIT_METHOD: 5,
            CodePattern.IF_NOT_NONE: 5,
            CodePattern.PROPERTY_GETTER: 4,
            CodePattern.RETURN_NONE: 4,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.IF_EMPTY_CHECK: 4, CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.RETURN_NONE, CodePattern.RETURN_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 141,
            CodePattern.RETURN_BOOL: 9,
            CodePattern.RETURN_NONE: 8,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.RETURN_LIST: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {
            CodePattern.RETURN_COMPUTED: 57,
            CodePattern.RETURN_LIST: 11,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.RETURN_NONE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 4, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LOOP_ZIP): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOOP_ZIP): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOOP_ENUMERATE): Counter(
        {CodePattern.DICT_GET_DEFAULT: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 5}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_LIST): Counter(
        {
            CodePattern.RETURN_LIST: 26,
            CodePattern.LOGGING_CALL: 25,
            CodePattern.GUARD_CLAUSE: 20,
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.INIT_EMPTY_LIST: 11,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.UNPACKING: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.RETURN_LIST, CodePattern.RETURN_LIST): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 14,
            CodePattern.LOGGING_CALL: 10,
            CodePattern.INIT_METHOD: 4,
            CodePattern.RETURN_LIST: 3,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3, CodePattern.IF_NOT_NONE: 3}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.PROPERTY_GETTER: 119,
            CodePattern.FUNCTION_TRANSFORMER: 48,
            CodePattern.INIT_METHOD: 15,
            CodePattern.GENERATOR_EXPRESSION: 12,
            CodePattern.LOGGING_CALL: 7,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.FUNCTION_VALIDATOR: 4,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 13, CodePattern.LOOP_DICT_ITEMS: 5}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.INIT_COUNTER): Counter(
        {
            CodePattern.INIT_COUNTER: 66,
            CodePattern.INIT_DEFAULT_VALUE: 48,
            CodePattern.INIT_METHOD: 13,
            CodePattern.FUNCTION_TRANSFORMER: 9,
            CodePattern.INIT_EMPTY_LIST: 8,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.LIST_COMPREHENSION: 10,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.INIT_EMPTY_LIST: 5,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 7}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 4}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_COUNTER): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 13,
            CodePattern.INIT_METHOD: 9,
            CodePattern.INIT_DEFAULT_VALUE: 8,
            CodePattern.INIT_COUNTER: 8,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 8, CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.LOOP_DICT_ITEMS: 5, CodePattern.CONTEXT_MANAGER: 5}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.LOOP_DICT_ITEMS: 4, CodePattern.LIST_COMPREHENSION: 3}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.PROPERTY_GETTER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 107,
            CodePattern.LOGGING_CALL: 28,
            CodePattern.INIT_DEFAULT_VALUE: 12,
            CodePattern.CONTEXT_MANAGER: 8,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 11, CodePattern.INIT_DEFAULT_VALUE: 4}
    ),
    (CodePattern.INIT_METHOD, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.LOGGING_CALL: 5}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NOT_NONE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 41,
            CodePattern.IF_EMPTY_CHECK: 9,
            CodePattern.IF_NOT_NONE: 6,
            CodePattern.CONTEXT_MANAGER: 5,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.RETURN_BOOL, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.LOGGING_CALL: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.LOGGING_CALL: 4,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.STRING_FORMAT: 4}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.INIT_METHOD: 16,
            CodePattern.FUNCTION_TRANSFORMER: 9,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.UNPACKING): Counter(
        {
            CodePattern.DICT_GET_DEFAULT: 22,
            CodePattern.UNPACKING: 14,
            CodePattern.CONTEXT_MANAGER: 5,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 38,
            CodePattern.RETURN_COMPUTED: 20,
            CodePattern.TERNARY_EXPRESSION: 13,
            CodePattern.LIST_COMPREHENSION: 10,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.INIT_METHOD: 4,
            CodePattern.INIT_EMPTY_LIST: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.LOOP_FILTER, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 26, CodePattern.STRING_FORMAT: 5}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.TERNARY_EXPRESSION: 6,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.IF_NOT_NONE): Counter(
        {
            CodePattern.IF_NOT_NONE: 10,
            CodePattern.FUNCTION_TRANSFORMER: 8,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.UNPACKING: 4,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.IF_NOT_NONE): Counter(
        {
            CodePattern.IF_NOT_NONE: 37,
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.FUNCTION_TRANSFORMER: 12,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.UNPACKING: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.UNPACKING): Counter(
        {CodePattern.IF_NOT_NONE: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.RETURN_COMPUTED: 5, CodePattern.CONTEXT_MANAGER: 4}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.DICT_GET_DEFAULT: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 4, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.RETURN_COMPUTED: 6}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.DICT_COMPREHENSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 12,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.TERNARY_EXPRESSION: 4,
        }
    ),
    (CodePattern.DICT_COMPREHENSION, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.DICT_GET_DEFAULT): Counter(
        {CodePattern.DICT_GET_DEFAULT: 6, CodePattern.IF_EMPTY_CHECK: 6}
    ),
    (CodePattern.UNPACKING, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.RETURN_NONE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_DICT): Counter(
        {CodePattern.RETURN_COMPUTED: 3, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.LOOP_ENUMERATE, CodePattern.LOOP_ENUMERATE): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_ENUMERATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.LOOP_ACCUMULATE: 5,
            CodePattern.INIT_DEFAULT_VALUE: 4,
        }
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.GENERATOR_EXPRESSION: 27,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.INIT_EMPTY_LIST: 8,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.UNPACKING: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_NONE): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_BOOL: 41, CodePattern.RETURN_COMPUTED: 9}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_TRANSFORM): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.RETURN_COMPUTED: 8, CodePattern.RETURN_BOOL: 5}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 36,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.CLASS_METHOD: 14, CodePattern.FUNCTION_TRANSFORMER: 6}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.CONTEXT_MANAGER: 4}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 6, CodePattern.RETURN_BOOL: 4}
    ),
    (CodePattern.INIT_METHOD, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 8}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.UNPACKING): Counter(
        {CodePattern.RETURN_COMPUTED: 7, CodePattern.UNPACKING: 6}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.INIT_EMPTY_LIST: 6,
            CodePattern.LOOP_FILTER: 5,
            CodePattern.INIT_COUNTER: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.CLASS_METHOD, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.CLASS_METHOD: 4,
            CodePattern.RETURN_LIST: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 46,
            CodePattern.RETURN_COMPUTED: 31,
            CodePattern.FUNCTION_TRANSFORMER: 18,
            CodePattern.LOGGING_CALL: 12,
            CodePattern.TERNARY_EXPRESSION: 8,
            CodePattern.GENERATOR_EXPRESSION: 8,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.LOOP_DICT_ITEMS: 4,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.GUARD_CLAUSE: 3,
            CodePattern.UNPACKING: 3,
            CodePattern.IF_NONE_CHECK: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.FUNCTION_VALIDATOR): Counter(
        {CodePattern.GUARD_CLAUSE: 4, CodePattern.IF_NONE_CHECK: 4}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 6,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.UNPACKING: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.CONTEXT_MANAGER: 3,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.LOGGING_CALL, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 30,
            CodePattern.CLASS_METHOD: 13,
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.LOGGING_CALL: 6,
            CodePattern.FUNCTION_VALIDATOR: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_ENUMERATE): Counter(
        {CodePattern.LIST_COMPREHENSION: 6}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 3}
    ),
    (CodePattern.DICT_COMPREHENSION, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.LOOP_DICT_ITEMS: 3,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.CONTEXT_MANAGER: 3, CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.RETURN_NONE, CodePattern.DICT_GET_DEFAULT): Counter(
        {CodePattern.DICT_GET_DEFAULT: 4}
    ),
    (CodePattern.LOOP_ZIP, CodePattern.LOOP_ZIP): Counter(
        {
            CodePattern.LOOP_ZIP: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_BOOL: 4}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 4}
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 12,
            CodePattern.UNPACKING: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.RETURN_NONE, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_NONE: 23,
            CodePattern.RETURN_COMPUTED: 21,
            CodePattern.GUARD_CLAUSE: 5,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LOOP_ZIP): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.IF_TYPE_CHECK: 29,
            CodePattern.FUNCTION_TRANSFORMER: 12,
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.IF_EMPTY_CHECK: 9,
            CodePattern.UNPACKING: 8,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.UNPACKING: 4,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.RETURN_LIST, CodePattern.UNPACKING): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 7}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 8,
            CodePattern.IF_TYPE_CHECK: 8,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.LIST_COMPREHENSION: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 11, CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 12, CodePattern.RETURN_BOOL: 5}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 25,
            CodePattern.TERNARY_EXPRESSION: 12,
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.PROPERTY_GETTER: 9,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.INIT_METHOD: 3,
        }
    ),
    (CodePattern.DICT_COMPREHENSION, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 16, CodePattern.INIT_METHOD: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.DICT_COMPREHENSION): Counter(
        {CodePattern.DICT_COMPREHENSION: 5}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 11, CodePattern.CLASS_METHOD: 4}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.LOOP_ENUMERATE): Counter(
        {CodePattern.STRING_FORMAT: 4}
    ),
    (CodePattern.LOOP_ENUMERATE, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.LOOP_ENUMERATE: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 16,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 21}
    ),
    (CodePattern.DICT_COMPREHENSION, CodePattern.DICT_COMPREHENSION): Counter(
        {CodePattern.DICT_COMPREHENSION: 5, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 7}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NOT_NONE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.GUARD_CLAUSE: 5,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_EMPTY_DICT): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 5, CodePattern.UNPACKING: 3}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 7}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.LOOP_FILTER: 5}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.UNPACKING, CodePattern.TRY_EXCEPT_PASS): Counter(
        {CodePattern.UNPACKING: 3, CodePattern.TERNARY_EXPRESSION: 3}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.PROPERTY_GETTER): Counter(
        {
            CodePattern.PROPERTY_GETTER: 23,
            CodePattern.RETURN_COMPUTED: 18,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_DICT): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.RETURN_NONE, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.CLASS_METHOD, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 7}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.UNPACKING: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 22}
    ),
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.RETURN_LIST): Counter(
        {CodePattern.LOGGING_CALL: 17}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_LIST): Counter(
        {
            CodePattern.LOGGING_CALL: 13,
            CodePattern.INIT_EMPTY_LIST: 9,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.RETURN_LIST: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 7,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.UNPACKING: 4}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.UNPACKING): Counter(
        {CodePattern.DICT_GET_DEFAULT: 4, CodePattern.UNPACKING: 3}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 10, CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 4}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.RETURN_LIST): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 40,
            CodePattern.LOGGING_CALL: 6,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_NONE): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 30,
            CodePattern.PROPERTY_GETTER: 6,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.INIT_METHOD: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 71,
            CodePattern.INIT_DEFAULT_VALUE: 12,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.INIT_METHOD: 6,
            CodePattern.FUNCTION_VALIDATOR: 5,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.PROPERTY_GETTER: 3,
        }
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.DICT_GET_DEFAULT): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 4}
    ),
    (CodePattern.STATIC_METHOD, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.RETURN_LIST: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.RETURN_LIST, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 8, CodePattern.RETURN_LIST: 5}
    ),
    (CodePattern.RETURN_LIST, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_LIST: 24}
    ),
    (CodePattern.RETURN_LIST, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_LIST: 3}
    ),
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.RETURN_LIST: 3}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.RETURN_LIST): Counter(
        {CodePattern.LOGGING_CALL: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.GENERATOR_EXPRESSION: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 9,
            CodePattern.TERNARY_EXPRESSION: 6,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 8,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.INIT_EMPTY_LIST: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOOP_DICT_ITEMS): Counter(
        {CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_DICT): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.RETURN_DICT, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.GENERATOR_EXPRESSION: 6}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.LOOP_FILTER: 5, CodePattern.LOOP_ACCUMULATE: 4}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 14}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.RETURN_BOOL: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 5, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_LIST): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 21}
    ),
    (CodePattern.LOOP_ENUMERATE, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6}
    ),
    (CodePattern.INIT_METHOD, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.IF_NOT_NONE: 6, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 13,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.INIT_METHOD: 4,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.IF_TYPE_CHECK: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 9}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_NOT_NONE): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.LOOP_ENUMERATE, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.LIST_COMPREHENSION: 6}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.TRY_EXCEPT_PASS): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5, CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.RETURN_LIST: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_LIST): Counter(
        {CodePattern.IF_EMPTY_CHECK: 8, CodePattern.INIT_EMPTY_LIST: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.TRY_EXCEPT_RERAISE: 3, CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 52,
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.INIT_METHOD: 5,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_FILTER): Counter(
        {CodePattern.RETURN_COMPUTED: 4, CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 4, CodePattern.LOGGING_CALL: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 7, CodePattern.INIT_DEFAULT_VALUE: 4}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.GENERATOR_EXPRESSION: 3, CodePattern.INIT_EMPTY_LIST: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.GENERATOR_EXPRESSION: 5,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.IF_TYPE_CHECK: 8,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.UNPACKING: 7,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 7}
    ),
    (CodePattern.INIT_METHOD, CodePattern.IF_NOT_NONE): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 12,
            CodePattern.IF_NOT_NONE: 8,
            CodePattern.IF_NONE_CHECK: 4,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.RETURN_COMPUTED: 6, CodePattern.UNPACKING: 4}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.RETURN_COMPUTED: 35, CodePattern.TRY_EXCEPT_RERAISE: 6}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.RETURN_COMPUTED: 5, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.IF_NOT_NONE: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.RETURN_LIST): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 8, CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.GUARD_CLAUSE: 4, CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3, CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.UNPACKING: 4, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.IF_NONE_CHECK: 11,
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.UNPACKING: 4,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.INIT_EMPTY_DICT: 3,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.IF_EMPTY_CHECK: 5,
        }
    ),
    (CodePattern.LOOP_FILTER, CodePattern.LOOP_FILTER): Counter(
        {
            CodePattern.LOOP_FILTER: 6,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.STRING_FORMAT: 4,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.UNPACKING: 4}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_TRANSFORM: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_NONE, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.RETURN_COMPUTED: 6}
    ),
    (CodePattern.INIT_METHOD, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 23,
            CodePattern.IF_EMPTY_CHECK: 14,
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.IF_TYPE_CHECK: 5,
        }
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.IF_TYPE_CHECK: 5}
    ),
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_VALIDATOR): Counter(
        {CodePattern.GUARD_CLAUSE: 4}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 4}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 4, CodePattern.TRY_EXCEPT_RERAISE: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 17,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.RETURN_NONE: 12,
            CodePattern.RETURN_LIST: 4,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.RETURN_LIST, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.LOOP_FILTER: 11,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.IF_EMPTY_CHECK: 4,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 7}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.LOOP_FILTER, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 12,
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.LOGGING_CALL: 8,
            CodePattern.GENERATOR_EXPRESSION: 4,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.INIT_EMPTY_LIST: 5}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LOOP_FILTER): Counter(
        {CodePattern.LOGGING_CALL: 3}
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.UNPACKING): Counter(
        {CodePattern.STRING_FORMAT: 5, CodePattern.UNPACKING: 5}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.TERNARY_EXPRESSION: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_LIST: 8, CodePattern.LIST_COMPREHENSION: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.DICT_COMPREHENSION): Counter(
        {CodePattern.IF_TYPE_CHECK: 3}
    ),
    (CodePattern.DICT_COMPREHENSION, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 5}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.LOOP_ACCUMULATE: 4,
            CodePattern.IF_NOT_NONE: 3,
        }
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 6, CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.LOGGING_CALL: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.INIT_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.TRY_EXCEPT_PASS): Counter(
        {CodePattern.IF_TYPE_CHECK: 4}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.LOGGING_CALL: 4,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.TRY_EXCEPT_PASS): Counter(
        {CodePattern.RETURN_COMPUTED: 4, CodePattern.TRY_EXCEPT_PASS: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.RETURN_NONE: 4,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.RETURN_COMPUTED: 4, CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.RETURN_COMPUTED: 8, CodePattern.LOGGING_CALL: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.UNPACKING: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.INIT_COUNTER: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.UNPACKING): Counter(
        {
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 3}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.LOOP_FILTER): Counter(
        {CodePattern.LOOP_FILTER: 3}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_FILTER): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_NONE, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.RETURN_BOOL: 6}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.LOOP_FILTER): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 7, CodePattern.LOOP_TRANSFORM: 4}
    ),
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 5, CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 6, CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.RETURN_COMPUTED: 6}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.DICT_COMPREHENSION): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.IF_EMPTY_CHECK: 6,
            CodePattern.LOGGING_CALL: 5,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_DICT_ITEMS: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.LOGGING_CALL: 7}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 12, CodePattern.RETURN_NONE: 5}
    ),
    (CodePattern.RETURN_NONE, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_EXCEPT_PASS): Counter(
        {
            CodePattern.RETURN_COMPUTED: 16,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.TERNARY_EXPRESSION: 3,
            CodePattern.TRY_EXCEPT_PASS: 3,
        }
    ),
    (CodePattern.RETURN_BOOL, CodePattern.FUNCTION_VALIDATOR): Counter(
        {CodePattern.GUARD_CLAUSE: 4}
    ),
    (CodePattern.RETURN_NONE, CodePattern.TRY_EXCEPT_PASS): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 9,
            CodePattern.GUARD_CLAUSE: 5,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.IF_NONE_CHECK: 3,
        }
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 10}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.RETURN_BOOL: 4,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_BOOL): Counter(
        {
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.RETURN_BOOL: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_DICT): Counter(
        {CodePattern.DICT_COMPREHENSION: 3}
    ),
    (CodePattern.RETURN_DICT, CodePattern.DICT_COMPREHENSION): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.RETURN_LIST): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.INIT_METHOD): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.TRY_EXCEPT_LOG): Counter(
        {CodePattern.LOGGING_CALL: 5}
    ),
    (CodePattern.TRY_EXCEPT_LOG, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.LOGGING_CALL: 9, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.TRY_EXCEPT_LOG): Counter(
        {CodePattern.LOGGING_CALL: 4}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 21,
            CodePattern.RETURN_NONE: 5,
            CodePattern.RETURN_BOOL: 5,
            CodePattern.RETURN_LIST: 5,
        }
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.GUARD_CLAUSE: 4}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.LOGGING_CALL: 5, CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_LIST): Counter(
        {
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.LOGGING_CALL: 3,
        }
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.UNPACKING): Counter(
        {CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.STRING_FORMAT: 4, CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.RETURN_DICT): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.RETURN_NONE, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.INIT_EMPTY_DICT, CodePattern.TRY_EXCEPT_PASS): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 6}
    ),
    (CodePattern.UNPACKING, CodePattern.FUNCTION_VALIDATOR): Counter(
        {CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.INIT_EMPTY_LIST: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 6}
    ),
    (CodePattern.RETURN_NONE, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.UNPACKING: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.FUNCTION_VALIDATOR): Counter(
        {CodePattern.IF_EMPTY_CHECK: 3, CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.LOGGING_CALL: 4}
    ),
    (CodePattern.LOOP_ZIP, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.LIST_COMPREHENSION: 5}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.PROPERTY_GETTER: 6}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_LIST: 3}
    ),
    (CodePattern.CLASS_METHOD, CodePattern.INIT_EMPTY_DICT): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_LIST: 9}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.LOGGING_CALL: 5}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.FUNCTION_VALIDATOR): Counter(
        {CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.UNPACKING): Counter(
        {CodePattern.RETURN_COMPUTED: 7}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_ZIP): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_BOOL: 4}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.RETURN_LIST): Counter(
        {CodePattern.LOGGING_CALL: 5}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_LIST: 3}
    ),
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 6}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 7}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
}

# Pattern transition probabilities
probabilities = {
    (CodePattern.IF_EMPTY_CHECK, CodePattern.STRING_FORMAT): {
        CodePattern.RETURN_COMPUTED: 0.2647,
        CodePattern.GENERATOR_EXPRESSION: 0.2353,
        CodePattern.STRING_FORMAT: 0.1765,
        CodePattern.IF_EMPTY_CHECK: 0.1176,
        CodePattern.FUNCTION_TRANSFORMER: 0.1176,
        CodePattern.LIST_COMPREHENSION: 0.0882,
    },
    (CodePattern.STRING_FORMAT, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 0.4103,
        CodePattern.CONTEXT_MANAGER: 0.1987,
        CodePattern.UNPACKING: 0.0801,
        CodePattern.FUNCTION_TRANSFORMER: 0.0737,
        CodePattern.INIT_DEFAULT_VALUE: 0.0705,
        CodePattern.RETURN_COMPUTED: 0.0545,
        CodePattern.GENERATOR_EXPRESSION: 0.0224,
        CodePattern.TERNARY_EXPRESSION: 0.0192,
        CodePattern.LOOP_ACCUMULATE: 0.0160,
        CodePattern.INIT_EMPTY_LIST: 0.0128,
        CodePattern.IF_NONE_CHECK: 0.0128,
        CodePattern.TRY_FINALLY: 0.0096,
        CodePattern.IF_EMPTY_CHECK: 0.0096,
        CodePattern.LIST_COMPREHENSION: 0.0096,
    },
    (CodePattern.STRING_FORMAT, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.4236,
        CodePattern.STRING_FORMAT: 0.3399,
        CodePattern.INIT_DEFAULT_VALUE: 0.1281,
        CodePattern.UNPACKING: 0.0296,
        CodePattern.LOGGING_CALL: 0.0246,
        CodePattern.FUNCTION_TRANSFORMER: 0.0197,
        CodePattern.DICT_GET_DEFAULT: 0.0197,
        CodePattern.TERNARY_EXPRESSION: 0.0148,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.STRING_FORMAT): {
        CodePattern.CONTEXT_MANAGER: 0.4096,
        CodePattern.STRING_FORMAT: 0.2530,
        CodePattern.INIT_DEFAULT_VALUE: 0.1084,
        CodePattern.GENERATOR_EXPRESSION: 0.0763,
        CodePattern.LIST_COMPREHENSION: 0.0522,
        CodePattern.FUNCTION_TRANSFORMER: 0.0361,
        CodePattern.UNPACKING: 0.0281,
        CodePattern.DICT_GET_DEFAULT: 0.0201,
        CodePattern.RETURN_COMPUTED: 0.0161,
    },
    (CodePattern.STRING_FORMAT, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3233,
        CodePattern.FUNCTION_TRANSFORMER: 0.1729,
        CodePattern.GUARD_CLAUSE: 0.0827,
        CodePattern.INIT_EMPTY_LIST: 0.0827,
        CodePattern.IF_TYPE_CHECK: 0.0526,
        CodePattern.UNPACKING: 0.0526,
        CodePattern.IF_EMPTY_CHECK: 0.0451,
        CodePattern.RETURN_LIST: 0.0376,
        CodePattern.TERNARY_EXPRESSION: 0.0301,
        CodePattern.IF_NONE_CHECK: 0.0301,
        CodePattern.CONTEXT_MANAGER: 0.0226,
        CodePattern.INIT_DEFAULT_VALUE: 0.0226,
        CodePattern.STRING_FORMAT: 0.0226,
        CodePattern.INIT_COUNTER: 0.0226,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.3911,
        CodePattern.RETURN_NONE: 0.1546,
        CodePattern.IF_EMPTY_CHECK: 0.0609,
        CodePattern.FUNCTION_TRANSFORMER: 0.0515,
        CodePattern.RETURN_LIST: 0.0515,
        CodePattern.GUARD_CLAUSE: 0.0445,
        CodePattern.RETURN_BOOL: 0.0328,
        CodePattern.TERNARY_EXPRESSION: 0.0304,
        CodePattern.UNPACKING: 0.0304,
        CodePattern.IF_TYPE_CHECK: 0.0187,
        CodePattern.INIT_DEFAULT_VALUE: 0.0164,
        CodePattern.LIST_COMPREHENSION: 0.0164,
        CodePattern.RETURN_DICT: 0.0164,
        CodePattern.IF_NONE_CHECK: 0.0141,
        CodePattern.CONTEXT_MANAGER: 0.0141,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0117,
        CodePattern.STRING_FORMAT: 0.0094,
        CodePattern.TRY_EXCEPT_PASS: 0.0070,
        CodePattern.INIT_EMPTY_LIST: 0.0070,
        CodePattern.LOOP_ACCUMULATE: 0.0070,
        CodePattern.GENERATOR_EXPRESSION: 0.0070,
        CodePattern.IF_NOT_NONE: 0.0070,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3560,
        CodePattern.RETURN_COMPUTED: 0.2199,
        CodePattern.IF_EMPTY_CHECK: 0.0733,
        CodePattern.INIT_DEFAULT_VALUE: 0.0445,
        CodePattern.RETURN_LIST: 0.0366,
        CodePattern.GUARD_CLAUSE: 0.0314,
        CodePattern.TERNARY_EXPRESSION: 0.0262,
        CodePattern.PROPERTY_GETTER: 0.0262,
        CodePattern.STRING_FORMAT: 0.0209,
        CodePattern.IF_TYPE_CHECK: 0.0183,
        CodePattern.LIST_COMPREHENSION: 0.0183,
        CodePattern.UNPACKING: 0.0183,
        CodePattern.INIT_METHOD: 0.0131,
        CodePattern.LOOP_FILTER: 0.0131,
        CodePattern.INIT_EMPTY_LIST: 0.0131,
        CodePattern.FUNCTION_VALIDATOR: 0.0105,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0105,
        CodePattern.CLASS_METHOD: 0.0105,
        CodePattern.TRY_FINALLY: 0.0079,
        CodePattern.STATIC_METHOD: 0.0079,
        CodePattern.IF_NONE_CHECK: 0.0079,
        CodePattern.DICT_GET_DEFAULT: 0.0079,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0079,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.4545,
        CodePattern.FUNCTION_TRANSFORMER: 0.1313,
        CodePattern.IF_EMPTY_CHECK: 0.1111,
        CodePattern.STRING_FORMAT: 0.0404,
        CodePattern.UNPACKING: 0.0404,
        CodePattern.GUARD_CLAUSE: 0.0404,
        CodePattern.LIST_COMPREHENSION: 0.0303,
        CodePattern.LOGGING_CALL: 0.0303,
        CodePattern.IF_NONE_CHECK: 0.0303,
        CodePattern.IF_TYPE_CHECK: 0.0303,
        CodePattern.LOOP_ACCUMULATE: 0.0303,
        CodePattern.RETURN_LIST: 0.0303,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4222,
        CodePattern.FUNCTION_TRANSFORMER: 0.1007,
        CodePattern.GUARD_CLAUSE: 0.0702,
        CodePattern.IF_EMPTY_CHECK: 0.0600,
        CodePattern.IF_NONE_CHECK: 0.0419,
        CodePattern.UNPACKING: 0.0304,
        CodePattern.IF_TYPE_CHECK: 0.0252,
        CodePattern.INIT_EMPTY_LIST: 0.0249,
        CodePattern.TERNARY_EXPRESSION: 0.0242,
        CodePattern.INIT_DEFAULT_VALUE: 0.0193,
        CodePattern.LIST_COMPREHENSION: 0.0174,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0152,
        CodePattern.IF_NOT_NONE: 0.0146,
        CodePattern.CONTEXT_MANAGER: 0.0137,
        CodePattern.DICT_GET_DEFAULT: 0.0134,
        CodePattern.RETURN_LIST: 0.0109,
        CodePattern.INIT_EMPTY_DICT: 0.0109,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0090,
        CodePattern.LOOP_ACCUMULATE: 0.0087,
        CodePattern.RETURN_DICT: 0.0078,
        CodePattern.INIT_COUNTER: 0.0068,
        CodePattern.RETURN_BOOL: 0.0068,
        CodePattern.STRING_FORMAT: 0.0065,
        CodePattern.TRY_EXCEPT_PASS: 0.0059,
        CodePattern.GENERATOR_EXPRESSION: 0.0059,
        CodePattern.RETURN_NONE: 0.0050,
        CodePattern.INIT_METHOD: 0.0040,
        CodePattern.DICT_COMPREHENSION: 0.0034,
        CodePattern.LOOP_DICT_ITEMS: 0.0034,
        CodePattern.PROPERTY_GETTER: 0.0025,
        CodePattern.LOGGING_CALL: 0.0022,
        CodePattern.FUNCTION_VALIDATOR: 0.0022,
        CodePattern.LOOP_FILTER: 0.0016,
        CodePattern.TRY_FINALLY: 0.0012,
        CodePattern.LOOP_ENUMERATE: 0.0012,
        CodePattern.CLASS_METHOD: 0.0009,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.3085,
        CodePattern.RETURN_NONE: 0.2305,
        CodePattern.IF_NONE_CHECK: 0.0496,
        CodePattern.INIT_EMPTY_LIST: 0.0426,
        CodePattern.RETURN_LIST: 0.0426,
        CodePattern.IF_EMPTY_CHECK: 0.0390,
        CodePattern.INIT_EMPTY_DICT: 0.0390,
        CodePattern.FUNCTION_TRANSFORMER: 0.0319,
        CodePattern.INIT_DEFAULT_VALUE: 0.0248,
        CodePattern.DICT_GET_DEFAULT: 0.0213,
        CodePattern.UNPACKING: 0.0213,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0177,
        CodePattern.TRY_EXCEPT_PASS: 0.0177,
        CodePattern.IF_TYPE_CHECK: 0.0142,
        CodePattern.IF_NOT_NONE: 0.0142,
        CodePattern.TERNARY_EXPRESSION: 0.0142,
        CodePattern.RETURN_BOOL: 0.0142,
        CodePattern.LIST_COMPREHENSION: 0.0142,
        CodePattern.LOOP_ACCUMULATE: 0.0106,
        CodePattern.GUARD_CLAUSE: 0.0106,
        CodePattern.PROPERTY_GETTER: 0.0106,
        CodePattern.GENERATOR_EXPRESSION: 0.0106,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.RETURN_COMPUTED: 0.4375,
        CodePattern.IF_NONE_CHECK: 0.3750,
        CodePattern.IF_EMPTY_CHECK: 0.1875,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.5000,
        CodePattern.IF_EMPTY_CHECK: 0.1538,
        CodePattern.FUNCTION_TRANSFORMER: 0.1154,
        CodePattern.UNPACKING: 0.1154,
        CodePattern.GUARD_CLAUSE: 0.1154,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.3333,
        CodePattern.INIT_DEFAULT_VALUE: 0.2821,
        CodePattern.IF_EMPTY_CHECK: 0.2051,
        CodePattern.RETURN_COMPUTED: 0.1795,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.3043,
        CodePattern.FUNCTION_TRANSFORMER: 0.2609,
        CodePattern.INIT_DEFAULT_VALUE: 0.2174,
        CodePattern.IF_EMPTY_CHECK: 0.2174,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.2258,
        CodePattern.GENERATOR_EXPRESSION: 0.2258,
        CodePattern.IF_EMPTY_CHECK: 0.1935,
        CodePattern.RETURN_COMPUTED: 0.1290,
        CodePattern.LIST_COMPREHENSION: 0.1290,
        CodePattern.INIT_DEFAULT_VALUE: 0.0968,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4880,
        CodePattern.IF_EMPTY_CHECK: 0.0880,
        CodePattern.LIST_COMPREHENSION: 0.0880,
        CodePattern.CONTEXT_MANAGER: 0.0480,
        CodePattern.GUARD_CLAUSE: 0.0480,
        CodePattern.IF_TYPE_CHECK: 0.0400,
        CodePattern.FUNCTION_TRANSFORMER: 0.0320,
        CodePattern.UNPACKING: 0.0320,
        CodePattern.INIT_EMPTY_LIST: 0.0320,
        CodePattern.DICT_GET_DEFAULT: 0.0320,
        CodePattern.STRING_FORMAT: 0.0240,
        CodePattern.INIT_COUNTER: 0.0240,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0240,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.STRING_FORMAT): {
        CodePattern.RETURN_COMPUTED: 0.3611,
        CodePattern.STRING_FORMAT: 0.2500,
        CodePattern.GENERATOR_EXPRESSION: 0.1944,
        CodePattern.LIST_COMPREHENSION: 0.1944,
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.LIST_COMPREHENSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4615,
        CodePattern.LOOP_DICT_ITEMS: 0.3077,
        CodePattern.INIT_DEFAULT_VALUE: 0.2308,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3435,
        CodePattern.FUNCTION_TRANSFORMER: 0.1603,
        CodePattern.GUARD_CLAUSE: 0.0840,
        CodePattern.INIT_EMPTY_LIST: 0.0687,
        CodePattern.IF_EMPTY_CHECK: 0.0611,
        CodePattern.CONTEXT_MANAGER: 0.0458,
        CodePattern.UNPACKING: 0.0382,
        CodePattern.LIST_COMPREHENSION: 0.0305,
        CodePattern.IF_NONE_CHECK: 0.0305,
        CodePattern.INIT_DEFAULT_VALUE: 0.0229,
        CodePattern.RETURN_LIST: 0.0229,
        CodePattern.INIT_METHOD: 0.0229,
        CodePattern.DICT_COMPREHENSION: 0.0229,
        CodePattern.TERNARY_EXPRESSION: 0.0229,
        CodePattern.INIT_EMPTY_DICT: 0.0229,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.UNPACKING): {
        CodePattern.FUNCTION_TRANSFORMER: 0.1962,
        CodePattern.RETURN_COMPUTED: 0.1509,
        CodePattern.UNPACKING: 0.1208,
        CodePattern.INIT_DEFAULT_VALUE: 0.0868,
        CodePattern.GUARD_CLAUSE: 0.0830,
        CodePattern.IF_NOT_NONE: 0.0642,
        CodePattern.IF_EMPTY_CHECK: 0.0453,
        CodePattern.IF_TYPE_CHECK: 0.0340,
        CodePattern.IF_NONE_CHECK: 0.0302,
        CodePattern.TERNARY_EXPRESSION: 0.0302,
        CodePattern.STRING_FORMAT: 0.0189,
        CodePattern.INIT_METHOD: 0.0151,
        CodePattern.TRY_EXCEPT_PASS: 0.0151,
        CodePattern.LIST_COMPREHENSION: 0.0151,
        CodePattern.DICT_GET_DEFAULT: 0.0151,
        CodePattern.CONTEXT_MANAGER: 0.0151,
        CodePattern.LOOP_ACCUMULATE: 0.0151,
        CodePattern.RETURN_DICT: 0.0151,
        CodePattern.LOOP_FILTER: 0.0113,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0113,
        CodePattern.GENERATOR_EXPRESSION: 0.0113,
    },
    (CodePattern.UNPACKING, CodePattern.LOOP_FILTER): {
        CodePattern.IF_TYPE_CHECK: 1.0000
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 0.2857,
        CodePattern.TRY_EXCEPT_RERAISE: 0.2857,
        CodePattern.FUNCTION_TRANSFORMER: 0.2381,
        CodePattern.IF_EMPTY_CHECK: 0.1905,
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_COMPUTED: 0.4464,
        CodePattern.LOOP_ACCUMULATE: 0.1964,
        CodePattern.IF_EMPTY_CHECK: 0.0893,
        CodePattern.RETURN_NONE: 0.0714,
        CodePattern.GUARD_CLAUSE: 0.0714,
        CodePattern.STRING_FORMAT: 0.0714,
        CodePattern.UNPACKING: 0.0536,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.3810,
        CodePattern.LOOP_ACCUMULATE: 0.2857,
        CodePattern.STRING_FORMAT: 0.1905,
        CodePattern.RETURN_COMPUTED: 0.1429,
    },
    (CodePattern.UNPACKING, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.UNPACKING: 0.2500,
        CodePattern.RETURN_COMPUTED: 0.2500,
        CodePattern.FUNCTION_TRANSFORMER: 0.1250,
        CodePattern.GENERATOR_EXPRESSION: 0.1042,
        CodePattern.IF_EMPTY_CHECK: 0.0833,
        CodePattern.IF_NOT_NONE: 0.0625,
        CodePattern.LIST_COMPREHENSION: 0.0625,
        CodePattern.STRING_FORMAT: 0.0625,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.5455,
        CodePattern.INIT_DEFAULT_VALUE: 0.3182,
        CodePattern.INIT_METHOD: 0.1364,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4268,
        CodePattern.RETURN_COMPUTED: 0.1585,
        CodePattern.STRING_FORMAT: 0.1341,
        CodePattern.INIT_METHOD: 0.1220,
        CodePattern.INIT_DEFAULT_VALUE: 0.0732,
        CodePattern.CONTEXT_MANAGER: 0.0488,
        CodePattern.FUNCTION_VALIDATOR: 0.0366,
    },
    (CodePattern.UNPACKING, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4592,
        CodePattern.RETURN_COMPUTED: 0.1327,
        CodePattern.INIT_DEFAULT_VALUE: 0.1020,
        CodePattern.STRING_FORMAT: 0.0918,
        CodePattern.GENERATOR_EXPRESSION: 0.0510,
        CodePattern.PROPERTY_GETTER: 0.0510,
        CodePattern.UNPACKING: 0.0510,
        CodePattern.FUNCTION_VALIDATOR: 0.0306,
        CodePattern.RETURN_NONE: 0.0306,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.4286,
        CodePattern.IF_NONE_CHECK: 0.3571,
        CodePattern.IF_EMPTY_CHECK: 0.2143,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4114,
        CodePattern.RETURN_COMPUTED: 0.2089,
        CodePattern.IF_TYPE_CHECK: 0.0506,
        CodePattern.IF_EMPTY_CHECK: 0.0443,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0443,
        CodePattern.IF_NONE_CHECK: 0.0380,
        CodePattern.GUARD_CLAUSE: 0.0380,
        CodePattern.CONTEXT_MANAGER: 0.0316,
        CodePattern.PROPERTY_GETTER: 0.0316,
        CodePattern.INIT_DEFAULT_VALUE: 0.0253,
        CodePattern.STRING_FORMAT: 0.0190,
        CodePattern.LOOP_ACCUMULATE: 0.0190,
        CodePattern.INIT_METHOD: 0.0190,
        CodePattern.IF_NOT_NONE: 0.0190,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.4800,
        CodePattern.STRING_FORMAT: 0.2400,
        CodePattern.INIT_DEFAULT_VALUE: 0.1600,
        CodePattern.IF_EMPTY_CHECK: 0.1200,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.STRING_FORMAT): {
        CodePattern.LOOP_ACCUMULATE: 0.2778,
        CodePattern.RETURN_COMPUTED: 0.1944,
        CodePattern.FUNCTION_TRANSFORMER: 0.1667,
        CodePattern.IF_EMPTY_CHECK: 0.1389,
        CodePattern.STRING_FORMAT: 0.1111,
        CodePattern.GENERATOR_EXPRESSION: 0.1111,
    },
    (CodePattern.STRING_FORMAT, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.3158,
        CodePattern.STRING_FORMAT: 0.3158,
        CodePattern.RETURN_COMPUTED: 0.2105,
        CodePattern.INIT_DEFAULT_VALUE: 0.1579,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.3879,
        CodePattern.RETURN_COMPUTED: 0.2242,
        CodePattern.IF_EMPTY_CHECK: 0.0667,
        CodePattern.FUNCTION_TRANSFORMER: 0.0606,
        CodePattern.CONTEXT_MANAGER: 0.0545,
        CodePattern.INIT_DEFAULT_VALUE: 0.0424,
        CodePattern.STRING_FORMAT: 0.0364,
        CodePattern.TERNARY_EXPRESSION: 0.0303,
        CodePattern.DICT_GET_DEFAULT: 0.0242,
        CodePattern.UNPACKING: 0.0182,
        CodePattern.GUARD_CLAUSE: 0.0182,
        CodePattern.INIT_COUNTER: 0.0182,
        CodePattern.INIT_EMPTY_LIST: 0.0182,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.LOOP_ACCUMULATE: 0.3889,
        CodePattern.RETURN_COMPUTED: 0.3333,
        CodePattern.FUNCTION_TRANSFORMER: 0.2778,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3308,
        CodePattern.IF_EMPTY_CHECK: 0.1353,
        CodePattern.FUNCTION_TRANSFORMER: 0.1203,
        CodePattern.UNPACKING: 0.0677,
        CodePattern.GUARD_CLAUSE: 0.0602,
        CodePattern.IF_NONE_CHECK: 0.0602,
        CodePattern.INIT_DEFAULT_VALUE: 0.0526,
        CodePattern.IF_NOT_NONE: 0.0451,
        CodePattern.INIT_EMPTY_LIST: 0.0376,
        CodePattern.LIST_COMPREHENSION: 0.0226,
        CodePattern.INIT_COUNTER: 0.0226,
        CodePattern.IF_TYPE_CHECK: 0.0226,
        CodePattern.TERNARY_EXPRESSION: 0.0226,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_NONE): {
        CodePattern.GUARD_CLAUSE: 0.1484,
        CodePattern.RETURN_COMPUTED: 0.1484,
        CodePattern.FUNCTION_TRANSFORMER: 0.1355,
        CodePattern.IF_EMPTY_CHECK: 0.1032,
        CodePattern.IF_TYPE_CHECK: 0.0645,
        CodePattern.INIT_EMPTY_LIST: 0.0516,
        CodePattern.UNPACKING: 0.0452,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0452,
        CodePattern.LOGGING_CALL: 0.0387,
        CodePattern.INIT_DEFAULT_VALUE: 0.0323,
        CodePattern.TERNARY_EXPRESSION: 0.0323,
        CodePattern.TRY_FINALLY: 0.0194,
        CodePattern.CONTEXT_MANAGER: 0.0194,
        CodePattern.STRING_FORMAT: 0.0194,
        CodePattern.RETURN_NONE: 0.0194,
        CodePattern.LIST_COMPREHENSION: 0.0194,
        CodePattern.INIT_EMPTY_DICT: 0.0194,
        CodePattern.IF_NONE_CHECK: 0.0194,
        CodePattern.IF_NOT_NONE: 0.0194,
    },
    (CodePattern.RETURN_NONE, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 0.6250,
        CodePattern.FUNCTION_TRANSFORMER: 0.3750,
    },
    (CodePattern.LOGGING_CALL, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 0.5697,
        CodePattern.CONTEXT_MANAGER: 0.1091,
        CodePattern.INIT_DEFAULT_VALUE: 0.0758,
        CodePattern.DICT_GET_DEFAULT: 0.0727,
        CodePattern.FUNCTION_TRANSFORMER: 0.0485,
        CodePattern.RETURN_COMPUTED: 0.0394,
        CodePattern.LIST_COMPREHENSION: 0.0152,
        CodePattern.IF_EMPTY_CHECK: 0.0152,
        CodePattern.CLASS_METHOD: 0.0121,
        CodePattern.STRING_FORMAT: 0.0121,
        CodePattern.GENERATOR_EXPRESSION: 0.0121,
        CodePattern.TRY_FINALLY: 0.0091,
        CodePattern.IF_NOT_NONE: 0.0091,
    },
    (CodePattern.LOGGING_CALL, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LOGGING_CALL: 0.6667,
        CodePattern.LIST_COMPREHENSION: 0.3333,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 0.4286,
        CodePattern.CONTEXT_MANAGER: 0.1849,
        CodePattern.FUNCTION_TRANSFORMER: 0.0630,
        CodePattern.DICT_GET_DEFAULT: 0.0588,
        CodePattern.INIT_DEFAULT_VALUE: 0.0546,
        CodePattern.STRING_FORMAT: 0.0504,
        CodePattern.TERNARY_EXPRESSION: 0.0336,
        CodePattern.RETURN_COMPUTED: 0.0336,
        CodePattern.LOOP_ENUMERATE: 0.0252,
        CodePattern.CLASS_METHOD: 0.0210,
        CodePattern.IF_EMPTY_CHECK: 0.0168,
        CodePattern.LOOP_ZIP: 0.0168,
        CodePattern.LOOP_DICT_ITEMS: 0.0126,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 0.5556,
        CodePattern.DICT_GET_DEFAULT: 0.4444,
    },
    (CodePattern.LOGGING_CALL, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.LOGGING_CALL: 0.3333,
        CodePattern.TRY_EXCEPT_LOG: 0.1905,
        CodePattern.RETURN_LIST: 0.1905,
        CodePattern.RETURN_COMPUTED: 0.1429,
        CodePattern.RETURN_NONE: 0.1429,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 0.2143,
        CodePattern.RETURN_COMPUTED: 0.2143,
        CodePattern.STRING_FORMAT: 0.1786,
        CodePattern.IF_EMPTY_CHECK: 0.1786,
        CodePattern.CONTEXT_MANAGER: 0.1071,
        CodePattern.FUNCTION_TRANSFORMER: 0.1071,
    },
    (CodePattern.CLASS_METHOD, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.6627,
        CodePattern.INIT_DEFAULT_VALUE: 0.1205,
        CodePattern.DICT_GET_DEFAULT: 0.0964,
        CodePattern.LIST_COMPREHENSION: 0.0723,
        CodePattern.LOGGING_CALL: 0.0482,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.CONTEXT_MANAGER: 0.3966,
        CodePattern.DICT_GET_DEFAULT: 0.3621,
        CodePattern.INIT_DEFAULT_VALUE: 0.1056,
        CodePattern.IF_EMPTY_CHECK: 0.0409,
        CodePattern.CLASS_METHOD: 0.0237,
        CodePattern.UNPACKING: 0.0151,
        CodePattern.LIST_COMPREHENSION: 0.0129,
        CodePattern.STRING_FORMAT: 0.0129,
        CodePattern.LOGGING_CALL: 0.0129,
        CodePattern.TERNARY_EXPRESSION: 0.0108,
        CodePattern.GENERATOR_EXPRESSION: 0.0065,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.CONTEXT_MANAGER): {
        CodePattern.DICT_GET_DEFAULT: 0.4260,
        CodePattern.CONTEXT_MANAGER: 0.3636,
        CodePattern.LOGGING_CALL: 0.0831,
        CodePattern.INIT_DEFAULT_VALUE: 0.0571,
        CodePattern.LIST_COMPREHENSION: 0.0234,
        CodePattern.UNPACKING: 0.0130,
        CodePattern.CLASS_METHOD: 0.0130,
        CodePattern.STRING_FORMAT: 0.0104,
        CodePattern.FUNCTION_TRANSFORMER: 0.0104,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.6827,
        CodePattern.INIT_DEFAULT_VALUE: 0.1294,
        CodePattern.DICT_GET_DEFAULT: 0.0376,
        CodePattern.FUNCTION_TRANSFORMER: 0.0253,
        CodePattern.STRING_FORMAT: 0.0223,
        CodePattern.UNPACKING: 0.0187,
        CodePattern.LIST_COMPREHENSION: 0.0159,
        CodePattern.LOGGING_CALL: 0.0116,
        CodePattern.TRY_FINALLY: 0.0107,
        CodePattern.CLASS_METHOD: 0.0093,
        CodePattern.TERNARY_EXPRESSION: 0.0068,
        CodePattern.GENERATOR_EXPRESSION: 0.0064,
        CodePattern.INIT_EMPTY_LIST: 0.0043,
        CodePattern.TRY_EXCEPT_PASS: 0.0034,
        CodePattern.LOOP_DICT_ITEMS: 0.0030,
        CodePattern.IF_EMPTY_CHECK: 0.0027,
        CodePattern.INIT_METHOD: 0.0023,
        CodePattern.LOOP_ACCUMULATE: 0.0021,
        CodePattern.RETURN_COMPUTED: 0.0011,
        CodePattern.INIT_COUNTER: 0.0011,
        CodePattern.LOOP_ENUMERATE: 0.0009,
        CodePattern.LOOP_TRANSFORM: 0.0009,
        CodePattern.IF_NONE_CHECK: 0.0007,
        CodePattern.LOOP_ZIP: 0.0007,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.8089,
        CodePattern.INIT_DEFAULT_VALUE: 0.1245,
        CodePattern.FUNCTION_TRANSFORMER: 0.0110,
        CodePattern.DICT_GET_DEFAULT: 0.0102,
        CodePattern.UNPACKING: 0.0095,
        CodePattern.STRING_FORMAT: 0.0081,
        CodePattern.GENERATOR_EXPRESSION: 0.0059,
        CodePattern.TRY_FINALLY: 0.0044,
        CodePattern.CLASS_METHOD: 0.0037,
        CodePattern.LIST_COMPREHENSION: 0.0037,
        CodePattern.INIT_METHOD: 0.0037,
        CodePattern.IF_EMPTY_CHECK: 0.0022,
        CodePattern.INIT_EMPTY_LIST: 0.0022,
        CodePattern.TERNARY_EXPRESSION: 0.0022,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.4248,
        CodePattern.INIT_DEFAULT_VALUE: 0.3811,
        CodePattern.DICT_GET_DEFAULT: 0.0516,
        CodePattern.FUNCTION_TRANSFORMER: 0.0364,
        CodePattern.UNPACKING: 0.0194,
        CodePattern.STRING_FORMAT: 0.0164,
        CodePattern.CLASS_METHOD: 0.0121,
        CodePattern.LIST_COMPREHENSION: 0.0115,
        CodePattern.TRY_FINALLY: 0.0109,
        CodePattern.LOGGING_CALL: 0.0109,
        CodePattern.TERNARY_EXPRESSION: 0.0055,
        CodePattern.IF_EMPTY_CHECK: 0.0049,
        CodePattern.LOOP_ZIP: 0.0030,
        CodePattern.GENERATOR_EXPRESSION: 0.0030,
        CodePattern.INIT_EMPTY_LIST: 0.0024,
        CodePattern.LOOP_ACCUMULATE: 0.0024,
        CodePattern.INIT_METHOD: 0.0018,
        CodePattern.INIT_EMPTY_DICT: 0.0018,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.3077,
        CodePattern.CONTEXT_MANAGER: 0.2885,
        CodePattern.INIT_DEFAULT_VALUE: 0.2885,
        CodePattern.FUNCTION_TRANSFORMER: 0.0577,
        CodePattern.TERNARY_EXPRESSION: 0.0577,
    },
    (CodePattern.UNPACKING, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.6225,
        CodePattern.CONTEXT_MANAGER: 0.0778,
        CodePattern.INIT_DEFAULT_VALUE: 0.0712,
        CodePattern.FUNCTION_TRANSFORMER: 0.0563,
        CodePattern.RETURN_COMPUTED: 0.0265,
        CodePattern.DICT_GET_DEFAULT: 0.0248,
        CodePattern.STRING_FORMAT: 0.0166,
        CodePattern.LOOP_ACCUMULATE: 0.0149,
        CodePattern.LIST_COMPREHENSION: 0.0132,
        CodePattern.IF_NOT_NONE: 0.0132,
        CodePattern.TERNARY_EXPRESSION: 0.0116,
        CodePattern.IF_EMPTY_CHECK: 0.0099,
        CodePattern.GUARD_CLAUSE: 0.0099,
        CodePattern.LOGGING_CALL: 0.0083,
        CodePattern.INIT_EMPTY_LIST: 0.0066,
        CodePattern.IF_NONE_CHECK: 0.0066,
        CodePattern.DICT_COMPREHENSION: 0.0050,
        CodePattern.TRY_FINALLY: 0.0050,
    },
    (CodePattern.UNPACKING, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 0.3000,
        CodePattern.UNPACKING: 0.3000,
        CodePattern.CONTEXT_MANAGER: 0.2000,
        CodePattern.FUNCTION_TRANSFORMER: 0.1000,
        CodePattern.LOOP_ACCUMULATE: 0.1000,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.CONTEXT_MANAGER): {
        CodePattern.LIST_COMPREHENSION: 0.4129,
        CodePattern.CONTEXT_MANAGER: 0.3355,
        CodePattern.INIT_DEFAULT_VALUE: 0.0968,
        CodePattern.DICT_GET_DEFAULT: 0.0710,
        CodePattern.STRING_FORMAT: 0.0452,
        CodePattern.GENERATOR_EXPRESSION: 0.0194,
        CodePattern.TRY_FINALLY: 0.0194,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.7123,
        CodePattern.CONTEXT_MANAGER: 0.0761,
        CodePattern.FUNCTION_TRANSFORMER: 0.0588,
        CodePattern.INIT_COUNTER: 0.0461,
        CodePattern.INIT_METHOD: 0.0330,
        CodePattern.DICT_GET_DEFAULT: 0.0127,
        CodePattern.RETURN_COMPUTED: 0.0101,
        CodePattern.LOGGING_CALL: 0.0082,
        CodePattern.UNPACKING: 0.0067,
        CodePattern.STRING_FORMAT: 0.0056,
        CodePattern.CLASS_METHOD: 0.0049,
        CodePattern.TRY_FINALLY: 0.0030,
        CodePattern.LIST_COMPREHENSION: 0.0030,
        CodePattern.TERNARY_EXPRESSION: 0.0026,
        CodePattern.PROPERTY_GETTER: 0.0026,
        CodePattern.INIT_EMPTY_LIST: 0.0026,
        CodePattern.STATIC_METHOD: 0.0022,
        CodePattern.GUARD_CLAUSE: 0.0022,
        CodePattern.INIT_EMPTY_DICT: 0.0022,
        CodePattern.IF_EMPTY_CHECK: 0.0019,
        CodePattern.IF_NOT_NONE: 0.0015,
        CodePattern.LOOP_ACCUMULATE: 0.0015,
    },
    (CodePattern.CLASS_METHOD, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.7647,
        CodePattern.INIT_DEFAULT_VALUE: 0.2353,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.CONTEXT_MANAGER): {
        CodePattern.RETURN_COMPUTED: 0.3846,
        CodePattern.CONTEXT_MANAGER: 0.1678,
        CodePattern.FUNCTION_TRANSFORMER: 0.1469,
        CodePattern.GUARD_CLAUSE: 0.0629,
        CodePattern.UNPACKING: 0.0490,
        CodePattern.STRING_FORMAT: 0.0280,
        CodePattern.LIST_COMPREHENSION: 0.0280,
        CodePattern.INIT_EMPTY_LIST: 0.0280,
        CodePattern.INIT_DEFAULT_VALUE: 0.0210,
        CodePattern.TERNARY_EXPRESSION: 0.0210,
        CodePattern.LOGGING_CALL: 0.0210,
        CodePattern.RETURN_BOOL: 0.0210,
        CodePattern.IF_NONE_CHECK: 0.0210,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5181,
        CodePattern.CONTEXT_MANAGER: 0.1325,
        CodePattern.RETURN_COMPUTED: 0.1084,
        CodePattern.INIT_DEFAULT_VALUE: 0.0964,
        CodePattern.GENERATOR_EXPRESSION: 0.0602,
        CodePattern.STRING_FORMAT: 0.0482,
        CodePattern.LIST_COMPREHENSION: 0.0361,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6125,
        CodePattern.INIT_DEFAULT_VALUE: 0.0658,
        CodePattern.RETURN_COMPUTED: 0.0473,
        CodePattern.CONTEXT_MANAGER: 0.0408,
        CodePattern.STRING_FORMAT: 0.0348,
        CodePattern.INIT_METHOD: 0.0268,
        CodePattern.PROPERTY_GETTER: 0.0242,
        CodePattern.GENERATOR_EXPRESSION: 0.0238,
        CodePattern.DICT_GET_DEFAULT: 0.0170,
        CodePattern.FUNCTION_VALIDATOR: 0.0102,
        CodePattern.TERNARY_EXPRESSION: 0.0098,
        CodePattern.LOGGING_CALL: 0.0095,
        CodePattern.LIST_COMPREHENSION: 0.0091,
        CodePattern.GUARD_CLAUSE: 0.0091,
        CodePattern.UNPACKING: 0.0087,
        CodePattern.INIT_COUNTER: 0.0079,
        CodePattern.CLASS_METHOD: 0.0072,
        CodePattern.IF_EMPTY_CHECK: 0.0060,
        CodePattern.IF_NONE_CHECK: 0.0049,
        CodePattern.RETURN_NONE: 0.0038,
        CodePattern.INIT_EMPTY_LIST: 0.0030,
        CodePattern.STATIC_METHOD: 0.0030,
        CodePattern.LOOP_ACCUMULATE: 0.0026,
        CodePattern.IF_TYPE_CHECK: 0.0026,
        CodePattern.TRY_FINALLY: 0.0019,
        CodePattern.TRY_EXCEPT_PASS: 0.0019,
        CodePattern.RETURN_BOOL: 0.0019,
        CodePattern.LOOP_DICT_ITEMS: 0.0015,
        CodePattern.INIT_EMPTY_DICT: 0.0011,
        CodePattern.IF_NOT_NONE: 0.0011,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.STRING_FORMAT): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3085,
        CodePattern.GENERATOR_EXPRESSION: 0.2388,
        CodePattern.STRING_FORMAT: 0.1244,
        CodePattern.INIT_METHOD: 0.0746,
        CodePattern.RETURN_COMPUTED: 0.0746,
        CodePattern.LIST_COMPREHENSION: 0.0448,
        CodePattern.CONTEXT_MANAGER: 0.0348,
        CodePattern.INIT_DEFAULT_VALUE: 0.0348,
        CodePattern.GUARD_CLAUSE: 0.0299,
        CodePattern.PROPERTY_GETTER: 0.0199,
        CodePattern.CLASS_METHOD: 0.0149,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4615,
        CodePattern.INIT_COUNTER: 0.2670,
        CodePattern.FUNCTION_TRANSFORMER: 0.0860,
        CodePattern.INIT_METHOD: 0.0679,
        CodePattern.RETURN_COMPUTED: 0.0317,
        CodePattern.INIT_EMPTY_LIST: 0.0226,
        CodePattern.TERNARY_EXPRESSION: 0.0226,
        CodePattern.INIT_EMPTY_DICT: 0.0136,
        CodePattern.UNPACKING: 0.0136,
        CodePattern.PROPERTY_GETTER: 0.0136,
    },
    (CodePattern.INIT_COUNTER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4896,
        CodePattern.INIT_COUNTER: 0.2448,
        CodePattern.INIT_METHOD: 0.0885,
        CodePattern.FUNCTION_TRANSFORMER: 0.0729,
        CodePattern.CONTEXT_MANAGER: 0.0260,
        CodePattern.CLASS_METHOD: 0.0156,
        CodePattern.PROPERTY_GETTER: 0.0156,
        CodePattern.LIST_COMPREHENSION: 0.0156,
        CodePattern.LOOP_ACCUMULATE: 0.0156,
        CodePattern.INIT_EMPTY_LIST: 0.0156,
    },
    (CodePattern.CLASS_METHOD, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.6944,
        CodePattern.CONTEXT_MANAGER: 0.2222,
        CodePattern.INIT_DEFAULT_VALUE: 0.0833,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.6089,
        CodePattern.DICT_GET_DEFAULT: 0.2235,
        CodePattern.INIT_DEFAULT_VALUE: 0.1453,
        CodePattern.FUNCTION_TRANSFORMER: 0.0223,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.CLASS_METHOD): {
        CodePattern.CONTEXT_MANAGER: 0.3788,
        CodePattern.INIT_DEFAULT_VALUE: 0.1667,
        CodePattern.CLASS_METHOD: 0.1364,
        CodePattern.DICT_GET_DEFAULT: 0.1061,
        CodePattern.FUNCTION_TRANSFORMER: 0.0758,
        CodePattern.LOGGING_CALL: 0.0758,
        CodePattern.LIST_COMPREHENSION: 0.0606,
    },
    (CodePattern.STATIC_METHOD, CodePattern.RETURN_COMPUTED): {
        CodePattern.CLASS_METHOD: 0.4167,
        CodePattern.FUNCTION_TRANSFORMER: 0.3333,
        CodePattern.CONTEXT_MANAGER: 0.2500,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4517,
        CodePattern.RETURN_COMPUTED: 0.2184,
        CodePattern.INIT_METHOD: 0.0414,
        CodePattern.INIT_DEFAULT_VALUE: 0.0391,
        CodePattern.GENERATOR_EXPRESSION: 0.0264,
        CodePattern.PROPERTY_GETTER: 0.0253,
        CodePattern.GUARD_CLAUSE: 0.0218,
        CodePattern.FUNCTION_VALIDATOR: 0.0195,
        CodePattern.IF_EMPTY_CHECK: 0.0195,
        CodePattern.CONTEXT_MANAGER: 0.0172,
        CodePattern.STRING_FORMAT: 0.0172,
        CodePattern.IF_TYPE_CHECK: 0.0172,
        CodePattern.TERNARY_EXPRESSION: 0.0138,
        CodePattern.LIST_COMPREHENSION: 0.0115,
        CodePattern.INIT_COUNTER: 0.0103,
        CodePattern.TRY_FINALLY: 0.0069,
        CodePattern.IF_NOT_NONE: 0.0057,
        CodePattern.CLASS_METHOD: 0.0057,
        CodePattern.IF_NONE_CHECK: 0.0057,
        CodePattern.LOOP_DICT_ITEMS: 0.0046,
        CodePattern.DICT_GET_DEFAULT: 0.0034,
        CodePattern.UNPACKING: 0.0034,
        CodePattern.DICT_COMPREHENSION: 0.0034,
        CodePattern.LOOP_ACCUMULATE: 0.0034,
        CodePattern.RETURN_BOOL: 0.0034,
        CodePattern.LOGGING_CALL: 0.0034,
    },
    (CodePattern.UNPACKING, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.5312,
        CodePattern.UNPACKING: 0.2313,
        CodePattern.STRING_FORMAT: 0.0500,
        CodePattern.DICT_GET_DEFAULT: 0.0437,
        CodePattern.INIT_DEFAULT_VALUE: 0.0375,
        CodePattern.FUNCTION_TRANSFORMER: 0.0375,
        CodePattern.TRY_FINALLY: 0.0312,
        CodePattern.CLASS_METHOD: 0.0187,
        CodePattern.RETURN_COMPUTED: 0.0187,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.UNPACKING): {
        CodePattern.IF_EMPTY_CHECK: 0.3077,
        CodePattern.FUNCTION_TRANSFORMER: 0.2051,
        CodePattern.RETURN_COMPUTED: 0.1538,
        CodePattern.UNPACKING: 0.1026,
        CodePattern.INIT_DEFAULT_VALUE: 0.0769,
        CodePattern.STRING_FORMAT: 0.0769,
        CodePattern.DICT_GET_DEFAULT: 0.0769,
    },
    (CodePattern.UNPACKING, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.3010,
        CodePattern.INIT_DEFAULT_VALUE: 0.3010,
        CodePattern.FUNCTION_TRANSFORMER: 0.1650,
        CodePattern.UNPACKING: 0.1359,
        CodePattern.RETURN_COMPUTED: 0.0388,
        CodePattern.INIT_EMPTY_LIST: 0.0291,
        CodePattern.STRING_FORMAT: 0.0291,
    },
    (CodePattern.LOOP_ENUMERATE, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.3636,
        CodePattern.INIT_DEFAULT_VALUE: 0.3636,
        CodePattern.LIST_COMPREHENSION: 0.2727,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.UNPACKING): {
        CodePattern.CONTEXT_MANAGER: 0.4773,
        CodePattern.UNPACKING: 0.2898,
        CodePattern.INIT_DEFAULT_VALUE: 0.1250,
        CodePattern.FUNCTION_TRANSFORMER: 0.0341,
        CodePattern.STRING_FORMAT: 0.0284,
        CodePattern.LIST_COMPREHENSION: 0.0284,
        CodePattern.DICT_GET_DEFAULT: 0.0170,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.CONTEXT_MANAGER: 0.4074,
        CodePattern.LOOP_ACCUMULATE: 0.3704,
        CodePattern.INIT_DEFAULT_VALUE: 0.1111,
        CodePattern.LOOP_ZIP: 0.1111,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.4500,
        CodePattern.LOOP_ACCUMULATE: 0.3500,
        CodePattern.INIT_DEFAULT_VALUE: 0.2000,
    },
    (CodePattern.CLASS_METHOD, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 0.7333,
        CodePattern.CONTEXT_MANAGER: 0.2667,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LIST_COMPREHENSION): {
        CodePattern.CONTEXT_MANAGER: 0.4463,
        CodePattern.LIST_COMPREHENSION: 0.3164,
        CodePattern.INIT_DEFAULT_VALUE: 0.0678,
        CodePattern.FUNCTION_TRANSFORMER: 0.0678,
        CodePattern.GENERATOR_EXPRESSION: 0.0395,
        CodePattern.TERNARY_EXPRESSION: 0.0282,
        CodePattern.DICT_GET_DEFAULT: 0.0169,
        CodePattern.CLASS_METHOD: 0.0169,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.5714,
        CodePattern.CONTEXT_MANAGER: 0.2143,
        CodePattern.LIST_COMPREHENSION: 0.2143,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3874,
        CodePattern.RETURN_COMPUTED: 0.1858,
        CodePattern.INIT_DEFAULT_VALUE: 0.1067,
        CodePattern.CONTEXT_MANAGER: 0.0711,
        CodePattern.INIT_METHOD: 0.0593,
        CodePattern.GUARD_CLAUSE: 0.0277,
        CodePattern.DICT_GET_DEFAULT: 0.0198,
        CodePattern.UNPACKING: 0.0198,
        CodePattern.INIT_EMPTY_LIST: 0.0158,
        CodePattern.INIT_COUNTER: 0.0158,
        CodePattern.RETURN_LIST: 0.0158,
        CodePattern.IF_NONE_CHECK: 0.0158,
        CodePattern.RETURN_DICT: 0.0119,
        CodePattern.RETURN_NONE: 0.0119,
        CodePattern.IF_EMPTY_CHECK: 0.0119,
        CodePattern.PROPERTY_GETTER: 0.0119,
        CodePattern.RETURN_BOOL: 0.0119,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.LIST_COMPREHENSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4000,
        CodePattern.LIST_COMPREHENSION: 0.1800,
        CodePattern.RETURN_COMPUTED: 0.1600,
        CodePattern.TERNARY_EXPRESSION: 0.1000,
        CodePattern.CONTEXT_MANAGER: 0.0800,
        CodePattern.INIT_DEFAULT_VALUE: 0.0800,
    },
    (CodePattern.TRY_FINALLY, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.CLASS_METHOD, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.FUNCTION_TRANSFORMER: 0.4286,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4232,
        CodePattern.FUNCTION_TRANSFORMER: 0.2194,
        CodePattern.CONTEXT_MANAGER: 0.1348,
        CodePattern.INIT_METHOD: 0.1348,
        CodePattern.INIT_COUNTER: 0.0408,
        CodePattern.RETURN_COMPUTED: 0.0282,
        CodePattern.UNPACKING: 0.0094,
        CodePattern.CLASS_METHOD: 0.0094,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.CLASS_METHOD): {
        CodePattern.CONTEXT_MANAGER: 0.4783,
        CodePattern.FUNCTION_TRANSFORMER: 0.2174,
        CodePattern.DICT_GET_DEFAULT: 0.1739,
        CodePattern.INIT_DEFAULT_VALUE: 0.1304,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.7044,
        CodePattern.CONTEXT_MANAGER: 0.1077,
        CodePattern.INIT_DEFAULT_VALUE: 0.0584,
        CodePattern.LOGGING_CALL: 0.0429,
        CodePattern.CLASS_METHOD: 0.0204,
        CodePattern.FUNCTION_TRANSFORMER: 0.0155,
        CodePattern.UNPACKING: 0.0148,
        CodePattern.LIST_COMPREHENSION: 0.0106,
        CodePattern.INIT_EMPTY_LIST: 0.0049,
        CodePattern.STRING_FORMAT: 0.0042,
        CodePattern.TERNARY_EXPRESSION: 0.0028,
        CodePattern.RETURN_COMPUTED: 0.0028,
        CodePattern.LOOP_DICT_ITEMS: 0.0021,
        CodePattern.TRY_FINALLY: 0.0021,
        CodePattern.LOOP_ACCUMULATE: 0.0021,
        CodePattern.IF_EMPTY_CHECK: 0.0021,
        CodePattern.GUARD_CLAUSE: 0.0021,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.6250,
        CodePattern.STRING_FORMAT: 0.1562,
        CodePattern.LIST_COMPREHENSION: 0.0625,
        CodePattern.GENERATOR_EXPRESSION: 0.0625,
        CodePattern.FUNCTION_TRANSFORMER: 0.0469,
        CodePattern.DICT_GET_DEFAULT: 0.0469,
    },
    (CodePattern.CLASS_METHOD, CodePattern.CLASS_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.2800,
        CodePattern.CLASS_METHOD: 0.2800,
        CodePattern.CONTEXT_MANAGER: 0.2400,
        CodePattern.INIT_DEFAULT_VALUE: 0.2000,
    },
    (CodePattern.CLASS_METHOD, CodePattern.UNPACKING): {CodePattern.UNPACKING: 1.0000},
    (CodePattern.LIST_COMPREHENSION, CodePattern.CLASS_METHOD): {
        CodePattern.CONTEXT_MANAGER: 0.5714,
        CodePattern.LIST_COMPREHENSION: 0.4286,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.TRY_FINALLY): {
        CodePattern.CONTEXT_MANAGER: 0.6282,
        CodePattern.TRY_FINALLY: 0.1282,
        CodePattern.DICT_GET_DEFAULT: 0.0897,
        CodePattern.FUNCTION_TRANSFORMER: 0.0769,
        CodePattern.INIT_DEFAULT_VALUE: 0.0769,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.CLASS_METHOD): {
        CodePattern.LOGGING_CALL: 0.6364,
        CodePattern.DICT_GET_DEFAULT: 0.1591,
        CodePattern.CONTEXT_MANAGER: 0.1136,
        CodePattern.LIST_COMPREHENSION: 0.0909,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.4494,
        CodePattern.FUNCTION_TRANSFORMER: 0.1772,
        CodePattern.INIT_DEFAULT_VALUE: 0.1329,
        CodePattern.LOGGING_CALL: 0.0696,
        CodePattern.STRING_FORMAT: 0.0506,
        CodePattern.RETURN_COMPUTED: 0.0380,
        CodePattern.UNPACKING: 0.0316,
        CodePattern.DICT_GET_DEFAULT: 0.0316,
        CodePattern.GENERATOR_EXPRESSION: 0.0190,
    },
    (CodePattern.CLASS_METHOD, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.INIT_EMPTY_LIST: 0.5714,
        CodePattern.LOGGING_CALL: 0.4286,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.2727,
        CodePattern.INIT_EMPTY_LIST: 0.2273,
        CodePattern.LOOP_TRANSFORM: 0.1818,
        CodePattern.INIT_DEFAULT_VALUE: 0.1212,
        CodePattern.UNPACKING: 0.0606,
        CodePattern.CONTEXT_MANAGER: 0.0455,
        CodePattern.DICT_GET_DEFAULT: 0.0455,
        CodePattern.LOOP_ACCUMULATE: 0.0455,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_TRANSFORM): {
        CodePattern.RETURN_COMPUTED: 0.2500,
        CodePattern.UNPACKING: 0.2143,
        CodePattern.STRING_FORMAT: 0.1607,
        CodePattern.CONTEXT_MANAGER: 0.0893,
        CodePattern.FUNCTION_TRANSFORMER: 0.0893,
        CodePattern.LIST_COMPREHENSION: 0.0893,
        CodePattern.INIT_EMPTY_LIST: 0.0536,
        CodePattern.DICT_GET_DEFAULT: 0.0536,
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.LOOP_TRANSFORM): {
        CodePattern.LOOP_TRANSFORM: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.CLASS_METHOD, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.CONTEXT_MANAGER: 0.7000,
        CodePattern.INIT_DEFAULT_VALUE: 0.3000,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.CLASS_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4286,
        CodePattern.FUNCTION_TRANSFORMER: 0.2026,
        CodePattern.GUARD_CLAUSE: 0.0448,
        CodePattern.IF_EMPTY_CHECK: 0.0394,
        CodePattern.INIT_DEFAULT_VALUE: 0.0330,
        CodePattern.CONTEXT_MANAGER: 0.0320,
        CodePattern.IF_NONE_CHECK: 0.0299,
        CodePattern.RETURN_LIST: 0.0288,
        CodePattern.RETURN_BOOL: 0.0224,
        CodePattern.TERNARY_EXPRESSION: 0.0171,
        CodePattern.IF_TYPE_CHECK: 0.0139,
        CodePattern.RETURN_NONE: 0.0128,
        CodePattern.UNPACKING: 0.0117,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0107,
        CodePattern.IF_NOT_NONE: 0.0107,
        CodePattern.DICT_GET_DEFAULT: 0.0096,
        CodePattern.INIT_METHOD: 0.0064,
        CodePattern.LOOP_ACCUMULATE: 0.0064,
        CodePattern.INIT_EMPTY_DICT: 0.0053,
        CodePattern.LIST_COMPREHENSION: 0.0043,
        CodePattern.RETURN_DICT: 0.0043,
        CodePattern.INIT_EMPTY_LIST: 0.0043,
        CodePattern.TRY_EXCEPT_PASS: 0.0043,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0043,
        CodePattern.LOOP_DICT_ITEMS: 0.0032,
        CodePattern.LOGGING_CALL: 0.0032,
        CodePattern.STRING_FORMAT: 0.0032,
        CodePattern.INIT_COUNTER: 0.0032,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.CONTEXT_MANAGER: 0.2667,
        CodePattern.FUNCTION_TRANSFORMER: 0.2667,
        CodePattern.RETURN_COMPUTED: 0.2667,
        CodePattern.DICT_GET_DEFAULT: 0.2000,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.CONTEXT_MANAGER: 0.4800,
        CodePattern.INIT_DEFAULT_VALUE: 0.1600,
        CodePattern.GENERATOR_EXPRESSION: 0.1200,
        CodePattern.FUNCTION_TRANSFORMER: 0.1200,
        CodePattern.RETURN_COMPUTED: 0.1200,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.5000,
        CodePattern.INIT_DEFAULT_VALUE: 0.2812,
        CodePattern.RETURN_COMPUTED: 0.1250,
        CodePattern.LOGGING_CALL: 0.0938,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.IF_TYPE_CHECK): {
        CodePattern.STRING_FORMAT: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.STRING_FORMAT): {
        CodePattern.IF_TYPE_CHECK: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 0.3077,
        CodePattern.LIST_COMPREHENSION: 0.2308,
        CodePattern.IF_NONE_CHECK: 0.2308,
        CodePattern.FUNCTION_TRANSFORMER: 0.2308,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 0.2941,
        CodePattern.IF_EMPTY_CHECK: 0.2941,
        CodePattern.TERNARY_EXPRESSION: 0.2353,
        CodePattern.FUNCTION_TRANSFORMER: 0.1765,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.6136,
        CodePattern.INIT_DEFAULT_VALUE: 0.3182,
        CodePattern.LOOP_DICT_ITEMS: 0.0682,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.CONTEXT_MANAGER: 0.6964,
        CodePattern.TERNARY_EXPRESSION: 0.1964,
        CodePattern.FUNCTION_TRANSFORMER: 0.0536,
        CodePattern.INIT_DEFAULT_VALUE: 0.0536,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.4531,
        CodePattern.TERNARY_EXPRESSION: 0.1719,
        CodePattern.DICT_GET_DEFAULT: 0.1250,
        CodePattern.INIT_DEFAULT_VALUE: 0.1094,
        CodePattern.STRING_FORMAT: 0.0781,
        CodePattern.LIST_COMPREHENSION: 0.0625,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_METHOD): {
        CodePattern.CONTEXT_MANAGER: 0.4615,
        CodePattern.INIT_METHOD: 0.3077,
        CodePattern.FUNCTION_TRANSFORMER: 0.2308,
    },
    (CodePattern.INIT_METHOD, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4667,
        CodePattern.INIT_METHOD: 0.3333,
        CodePattern.CONTEXT_MANAGER: 0.1000,
        CodePattern.RETURN_COMPUTED: 0.1000,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_ZIP): {
        CodePattern.CONTEXT_MANAGER: 0.5455,
        CodePattern.LOOP_ZIP: 0.4545,
    },
    (CodePattern.LOOP_ZIP, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.3333,
        CodePattern.DICT_GET_DEFAULT: 0.3333,
        CodePattern.LOOP_ACCUMULATE: 0.3333,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.CONTEXT_MANAGER: 0.3077,
        CodePattern.LOOP_FILTER: 0.2308,
        CodePattern.LOOP_TRANSFORM: 0.1923,
        CodePattern.INIT_EMPTY_LIST: 0.1538,
        CodePattern.LOOP_ENUMERATE: 0.1154,
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6167,
        CodePattern.RETURN_COMPUTED: 0.2333,
        CodePattern.INIT_DEFAULT_VALUE: 0.1000,
        CodePattern.DICT_GET_DEFAULT: 0.0500,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.7857,
        CodePattern.INIT_DEFAULT_VALUE: 0.2143,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.LOOP_FILTER: 0.6250,
        CodePattern.INIT_EMPTY_LIST: 0.3750,
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.INIT_EMPTY_LIST: 0.6250,
        CodePattern.STRING_FORMAT: 0.3750,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.GENERATOR_EXPRESSION: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.GENERATOR_EXPRESSION: 0.3182,
        CodePattern.CONTEXT_MANAGER: 0.1818,
        CodePattern.RETURN_COMPUTED: 0.1212,
        CodePattern.IF_EMPTY_CHECK: 0.1061,
        CodePattern.LIST_COMPREHENSION: 0.0758,
        CodePattern.INIT_DEFAULT_VALUE: 0.0606,
        CodePattern.TERNARY_EXPRESSION: 0.0455,
        CodePattern.UNPACKING: 0.0455,
        CodePattern.FUNCTION_TRANSFORMER: 0.0455,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.GENERATOR_EXPRESSION: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.6000,
        CodePattern.INIT_DEFAULT_VALUE: 0.1667,
        CodePattern.TRY_FINALLY: 0.0889,
        CodePattern.FUNCTION_TRANSFORMER: 0.0667,
        CodePattern.UNPACKING: 0.0444,
        CodePattern.LOGGING_CALL: 0.0333,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOGGING_CALL): {
        CodePattern.CONTEXT_MANAGER: 0.3719,
        CodePattern.DICT_GET_DEFAULT: 0.2211,
        CodePattern.LOGGING_CALL: 0.2161,
        CodePattern.FUNCTION_TRANSFORMER: 0.0754,
        CodePattern.INIT_DEFAULT_VALUE: 0.0704,
        CodePattern.LIST_COMPREHENSION: 0.0302,
        CodePattern.UNPACKING: 0.0151,
    },
    (CodePattern.LOGGING_CALL, CodePattern.UNPACKING): {CodePattern.UNPACKING: 1.0000},
    (CodePattern.TRY_FINALLY, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 0.3182,
        CodePattern.CONTEXT_MANAGER: 0.2045,
        CodePattern.GENERATOR_EXPRESSION: 0.1364,
        CodePattern.INIT_DEFAULT_VALUE: 0.0909,
        CodePattern.UNPACKING: 0.0909,
        CodePattern.RETURN_COMPUTED: 0.0909,
        CodePattern.LIST_COMPREHENSION: 0.0682,
    },
    (CodePattern.STRING_FORMAT, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.6250,
        CodePattern.CONTEXT_MANAGER: 0.3750,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.TRY_FINALLY): {
        CodePattern.INIT_EMPTY_LIST: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.TRY_FINALLY: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.STRING_FORMAT): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.TRY_FINALLY): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.5070,
        CodePattern.INIT_DEFAULT_VALUE: 0.2817,
        CodePattern.STRING_FORMAT: 0.0986,
        CodePattern.INIT_COUNTER: 0.0704,
        CodePattern.FUNCTION_TRANSFORMER: 0.0423,
    },
    (CodePattern.STRING_FORMAT, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.2416,
        CodePattern.STRING_FORMAT: 0.2081,
        CodePattern.RETURN_COMPUTED: 0.1275,
        CodePattern.CONTEXT_MANAGER: 0.0872,
        CodePattern.LIST_COMPREHENSION: 0.0738,
        CodePattern.INIT_DEFAULT_VALUE: 0.0537,
        CodePattern.TERNARY_EXPRESSION: 0.0470,
        CodePattern.INIT_METHOD: 0.0403,
        CodePattern.LOGGING_CALL: 0.0403,
        CodePattern.RETURN_DICT: 0.0201,
        CodePattern.CLASS_METHOD: 0.0201,
        CodePattern.IF_EMPTY_CHECK: 0.0201,
        CodePattern.PROPERTY_GETTER: 0.0201,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3246,
        CodePattern.UNPACKING: 0.0885,
        CodePattern.FUNCTION_TRANSFORMER: 0.0852,
        CodePattern.GUARD_CLAUSE: 0.0623,
        CodePattern.IF_EMPTY_CHECK: 0.0590,
        CodePattern.RETURN_LIST: 0.0459,
        CodePattern.IF_NONE_CHECK: 0.0393,
        CodePattern.IF_TYPE_CHECK: 0.0295,
        CodePattern.INIT_EMPTY_LIST: 0.0295,
        CodePattern.LOOP_ACCUMULATE: 0.0262,
        CodePattern.LIST_COMPREHENSION: 0.0262,
        CodePattern.INIT_DEFAULT_VALUE: 0.0230,
        CodePattern.CONTEXT_MANAGER: 0.0230,
        CodePattern.INIT_METHOD: 0.0230,
        CodePattern.TERNARY_EXPRESSION: 0.0230,
        CodePattern.RETURN_BOOL: 0.0197,
        CodePattern.DICT_GET_DEFAULT: 0.0131,
        CodePattern.IF_NOT_NONE: 0.0131,
        CodePattern.INIT_EMPTY_DICT: 0.0131,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0131,
        CodePattern.RETURN_NONE: 0.0098,
        CodePattern.STRING_FORMAT: 0.0098,
    },
    (CodePattern.TRY_FINALLY, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.4167,
        CodePattern.CONTEXT_MANAGER: 0.3333,
        CodePattern.TRY_FINALLY: 0.2500,
    },
    (CodePattern.TRY_FINALLY, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4545,
        CodePattern.FUNCTION_TRANSFORMER: 0.2727,
        CodePattern.IF_EMPTY_CHECK: 0.2727,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.2637,
        CodePattern.RETURN_COMPUTED: 0.1194,
        CodePattern.INIT_EMPTY_LIST: 0.0945,
        CodePattern.LOOP_TRANSFORM: 0.0796,
        CodePattern.FUNCTION_TRANSFORMER: 0.0547,
        CodePattern.IF_EMPTY_CHECK: 0.0498,
        CodePattern.IF_NOT_NONE: 0.0448,
        CodePattern.LOGGING_CALL: 0.0398,
        CodePattern.CONTEXT_MANAGER: 0.0299,
        CodePattern.LOOP_ENUMERATE: 0.0299,
        CodePattern.IF_NONE_CHECK: 0.0249,
        CodePattern.LOOP_DICT_ITEMS: 0.0199,
        CodePattern.INIT_DEFAULT_VALUE: 0.0199,
        CodePattern.GENERATOR_EXPRESSION: 0.0199,
        CodePattern.UNPACKING: 0.0199,
        CodePattern.LOOP_ACCUMULATE: 0.0199,
        CodePattern.INIT_EMPTY_DICT: 0.0199,
        CodePattern.TRY_EXCEPT_PASS: 0.0199,
        CodePattern.INIT_COUNTER: 0.0149,
        CodePattern.GUARD_CLAUSE: 0.0149,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7143,
        CodePattern.INIT_DEFAULT_VALUE: 0.1429,
        CodePattern.CLASS_METHOD: 0.1429,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.TRY_FINALLY): {
        CodePattern.CONTEXT_MANAGER: 0.6250,
        CodePattern.FUNCTION_TRANSFORMER: 0.3750,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LIST_COMPREHENSION): {
        CodePattern.CONTEXT_MANAGER: 0.2400,
        CodePattern.INIT_DEFAULT_VALUE: 0.2000,
        CodePattern.LIST_COMPREHENSION: 0.1600,
        CodePattern.FUNCTION_TRANSFORMER: 0.1600,
        CodePattern.GENERATOR_EXPRESSION: 0.1200,
        CodePattern.STRING_FORMAT: 0.1200,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.TRY_FINALLY): {
        CodePattern.CONTEXT_MANAGER: 0.6250,
        CodePattern.LOGGING_CALL: 0.1875,
        CodePattern.TRY_FINALLY: 0.1875,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 0.4825,
        CodePattern.FUNCTION_TRANSFORMER: 0.2105,
        CodePattern.CONTEXT_MANAGER: 0.0965,
        CodePattern.RETURN_COMPUTED: 0.0965,
        CodePattern.INIT_DEFAULT_VALUE: 0.0351,
        CodePattern.IF_EMPTY_CHECK: 0.0263,
        CodePattern.GENERATOR_EXPRESSION: 0.0263,
        CodePattern.STRING_FORMAT: 0.0263,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3043,
        CodePattern.RETURN_COMPUTED: 0.2609,
        CodePattern.STRING_FORMAT: 0.1739,
        CodePattern.IF_EMPTY_CHECK: 0.1304,
        CodePattern.GENERATOR_EXPRESSION: 0.1304,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.INIT_DEFAULT_VALUE: 0.3939,
        CodePattern.FUNCTION_TRANSFORMER: 0.1818,
        CodePattern.INIT_EMPTY_LIST: 0.1515,
        CodePattern.INIT_COUNTER: 0.0909,
        CodePattern.UNPACKING: 0.0909,
        CodePattern.LOOP_FILTER: 0.0909,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.STATIC_METHOD): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.5321,
        CodePattern.INIT_DEFAULT_VALUE: 0.2018,
        CodePattern.CONTEXT_MANAGER: 0.1101,
        CodePattern.FUNCTION_TRANSFORMER: 0.0550,
        CodePattern.STRING_FORMAT: 0.0550,
        CodePattern.LOGGING_CALL: 0.0459,
    },
    (CodePattern.LOGGING_CALL, CodePattern.CONTEXT_MANAGER): {
        CodePattern.LOGGING_CALL: 0.6033,
        CodePattern.CONTEXT_MANAGER: 0.2562,
        CodePattern.DICT_GET_DEFAULT: 0.0826,
        CodePattern.INIT_DEFAULT_VALUE: 0.0579,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_TYPE_CHECK): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.CONTEXT_MANAGER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.IF_NONE_CHECK): {
        CodePattern.IF_EMPTY_CHECK: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.LIST_COMPREHENSION): {
        CodePattern.STRING_FORMAT: 0.2791,
        CodePattern.FUNCTION_TRANSFORMER: 0.2558,
        CodePattern.INIT_DEFAULT_VALUE: 0.1163,
        CodePattern.RETURN_COMPUTED: 0.1163,
        CodePattern.CONTEXT_MANAGER: 0.0930,
        CodePattern.LIST_COMPREHENSION: 0.0698,
        CodePattern.TERNARY_EXPRESSION: 0.0698,
    },
    (CodePattern.INIT_COUNTER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.5000,
        CodePattern.IF_EMPTY_CHECK: 0.1190,
        CodePattern.RETURN_LIST: 0.0952,
        CodePattern.LOOP_ACCUMULATE: 0.0714,
        CodePattern.TERNARY_EXPRESSION: 0.0714,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0714,
        CodePattern.IF_NONE_CHECK: 0.0714,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_LIST): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6207,
        CodePattern.INIT_DEFAULT_VALUE: 0.1241,
        CodePattern.LOGGING_CALL: 0.0690,
        CodePattern.UNPACKING: 0.0621,
        CodePattern.CONTEXT_MANAGER: 0.0552,
        CodePattern.RETURN_LIST: 0.0345,
        CodePattern.FUNCTION_VALIDATOR: 0.0345,
    },
    (CodePattern.RETURN_LIST, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4667,
        CodePattern.CONTEXT_MANAGER: 0.3333,
        CodePattern.FUNCTION_TRANSFORMER: 0.2000,
    },
    (CodePattern.TRY_FINALLY, CodePattern.TRY_FINALLY): {
        CodePattern.TRY_FINALLY: 0.4000,
        CodePattern.CONTEXT_MANAGER: 0.4000,
        CodePattern.INIT_DEFAULT_VALUE: 0.2000,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_BOOL): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5930,
        CodePattern.INIT_DEFAULT_VALUE: 0.1395,
        CodePattern.RETURN_BOOL: 0.0930,
        CodePattern.RETURN_COMPUTED: 0.0581,
        CodePattern.CONTEXT_MANAGER: 0.0465,
        CodePattern.CLASS_METHOD: 0.0349,
        CodePattern.LOGGING_CALL: 0.0349,
    },
    (CodePattern.RETURN_BOOL, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.2911,
        CodePattern.FUNCTION_TRANSFORMER: 0.1076,
        CodePattern.TERNARY_EXPRESSION: 0.1076,
        CodePattern.GUARD_CLAUSE: 0.1076,
        CodePattern.IF_NONE_CHECK: 0.0633,
        CodePattern.INIT_EMPTY_LIST: 0.0506,
        CodePattern.IF_EMPTY_CHECK: 0.0506,
        CodePattern.UNPACKING: 0.0380,
        CodePattern.LIST_COMPREHENSION: 0.0316,
        CodePattern.CONTEXT_MANAGER: 0.0253,
        CodePattern.INIT_METHOD: 0.0253,
        CodePattern.IF_TYPE_CHECK: 0.0253,
        CodePattern.RETURN_DICT: 0.0190,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0190,
        CodePattern.IF_NOT_NONE: 0.0190,
        CodePattern.INIT_DEFAULT_VALUE: 0.0190,
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.IF_EMPTY_CHECK: 0.4545,
        CodePattern.IF_TYPE_CHECK: 0.2727,
        CodePattern.RETURN_COMPUTED: 0.2727,
    },
    (CodePattern.STATIC_METHOD, CodePattern.RETURN_BOOL): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_BOOL): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6567,
        CodePattern.RETURN_BOOL: 0.1493,
        CodePattern.STATIC_METHOD: 0.0597,
        CodePattern.INIT_METHOD: 0.0448,
        CodePattern.IF_EMPTY_CHECK: 0.0448,
        CodePattern.GUARD_CLAUSE: 0.0448,
    },
    (CodePattern.STATIC_METHOD, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.8421,
        CodePattern.STRING_FORMAT: 0.1579,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.STATIC_METHOD): {
        CodePattern.RETURN_COMPUTED: 0.7273,
        CodePattern.INIT_EMPTY_LIST: 0.2727,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_FILTER): {
        CodePattern.IF_EMPTY_CHECK: 0.2308,
        CodePattern.RETURN_COMPUTED: 0.1479,
        CodePattern.IF_TYPE_CHECK: 0.0888,
        CodePattern.LOOP_FILTER: 0.0828,
        CodePattern.UNPACKING: 0.0592,
        CodePattern.IF_NONE_CHECK: 0.0533,
        CodePattern.INIT_EMPTY_LIST: 0.0473,
        CodePattern.STRING_FORMAT: 0.0473,
        CodePattern.TERNARY_EXPRESSION: 0.0473,
        CodePattern.LOOP_ACCUMULATE: 0.0473,
        CodePattern.INIT_DEFAULT_VALUE: 0.0414,
        CodePattern.LOGGING_CALL: 0.0296,
        CodePattern.GUARD_CLAUSE: 0.0237,
        CodePattern.DICT_GET_DEFAULT: 0.0178,
        CodePattern.LOOP_DICT_ITEMS: 0.0178,
        CodePattern.GENERATOR_EXPRESSION: 0.0178,
    },
    (CodePattern.LOOP_FILTER, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5393,
        CodePattern.STRING_FORMAT: 0.1573,
        CodePattern.RETURN_COMPUTED: 0.1236,
        CodePattern.INIT_METHOD: 0.0562,
        CodePattern.INIT_DEFAULT_VALUE: 0.0449,
        CodePattern.GENERATOR_EXPRESSION: 0.0449,
        CodePattern.CONTEXT_MANAGER: 0.0337,
    },
    (CodePattern.INIT_COUNTER, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.5000,
        CodePattern.LOOP_ACCUMULATE: 0.5000,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.STATIC_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5762,
        CodePattern.LIST_COMPREHENSION: 0.0927,
        CodePattern.IF_TYPE_CHECK: 0.0795,
        CodePattern.IF_EMPTY_CHECK: 0.0530,
        CodePattern.INIT_EMPTY_LIST: 0.0397,
        CodePattern.GUARD_CLAUSE: 0.0331,
        CodePattern.UNPACKING: 0.0331,
        CodePattern.TERNARY_EXPRESSION: 0.0331,
        CodePattern.RETURN_LIST: 0.0331,
        CodePattern.FUNCTION_TRANSFORMER: 0.0265,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_COMPUTED): {
        CodePattern.IF_TYPE_CHECK: 0.3320,
        CodePattern.RETURN_COMPUTED: 0.2920,
        CodePattern.FUNCTION_TRANSFORMER: 0.2120,
        CodePattern.GUARD_CLAUSE: 0.0320,
        CodePattern.GENERATOR_EXPRESSION: 0.0280,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0240,
        CodePattern.INIT_METHOD: 0.0200,
        CodePattern.INIT_DEFAULT_VALUE: 0.0200,
        CodePattern.TERNARY_EXPRESSION: 0.0160,
        CodePattern.STRING_FORMAT: 0.0120,
        CodePattern.FUNCTION_VALIDATOR: 0.0120,
    },
    (CodePattern.CLASS_METHOD, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5476,
        CodePattern.RETURN_COMPUTED: 0.3571,
        CodePattern.IF_EMPTY_CHECK: 0.0952,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3834,
        CodePattern.IF_EMPTY_CHECK: 0.1347,
        CodePattern.INIT_DEFAULT_VALUE: 0.0933,
        CodePattern.TERNARY_EXPRESSION: 0.0777,
        CodePattern.IF_NONE_CHECK: 0.0777,
        CodePattern.RETURN_COMPUTED: 0.0570,
        CodePattern.IF_NOT_NONE: 0.0518,
        CodePattern.IF_TYPE_CHECK: 0.0311,
        CodePattern.LOOP_ACCUMULATE: 0.0207,
        CodePattern.INIT_METHOD: 0.0207,
        CodePattern.DICT_GET_DEFAULT: 0.0207,
        CodePattern.STRING_FORMAT: 0.0155,
        CodePattern.DICT_COMPREHENSION: 0.0155,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.CLASS_METHOD): {
        CodePattern.RETURN_COMPUTED: 0.2192,
        CodePattern.CLASS_METHOD: 0.1781,
        CodePattern.INIT_EMPTY_LIST: 0.1644,
        CodePattern.IF_EMPTY_CHECK: 0.1233,
        CodePattern.GUARD_CLAUSE: 0.0685,
        CodePattern.FUNCTION_TRANSFORMER: 0.0685,
        CodePattern.IF_TYPE_CHECK: 0.0548,
        CodePattern.INIT_DEFAULT_VALUE: 0.0411,
        CodePattern.LIST_COMPREHENSION: 0.0411,
        CodePattern.INIT_EMPTY_DICT: 0.0411,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.INIT_DEFAULT_VALUE: 0.2500,
        CodePattern.CONTEXT_MANAGER: 0.2500,
        CodePattern.LOOP_ACCUMULATE: 0.2500,
        CodePattern.FUNCTION_TRANSFORMER: 0.2500,
    },
    (CodePattern.LOOP_FILTER, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.3684,
        CodePattern.UNPACKING: 0.3158,
        CodePattern.LOOP_ACCUMULATE: 0.1579,
        CodePattern.IF_TYPE_CHECK: 0.1579,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LIST_COMPREHENSION): {
        CodePattern.DICT_GET_DEFAULT: 0.4333,
        CodePattern.LIST_COMPREHENSION: 0.3000,
        CodePattern.CONTEXT_MANAGER: 0.1333,
        CodePattern.LOGGING_CALL: 0.1333,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.7000,
        CodePattern.INIT_EMPTY_LIST: 0.3000,
    },
    (CodePattern.LOOP_FILTER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_LIST: 0.1609,
        CodePattern.GUARD_CLAUSE: 0.1437,
        CodePattern.RETURN_COMPUTED: 0.1322,
        CodePattern.IF_EMPTY_CHECK: 0.1322,
        CodePattern.INIT_EMPTY_LIST: 0.0747,
        CodePattern.IF_NONE_CHECK: 0.0632,
        CodePattern.FUNCTION_TRANSFORMER: 0.0575,
        CodePattern.UNPACKING: 0.0517,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0345,
        CodePattern.LIST_COMPREHENSION: 0.0345,
        CodePattern.INIT_DEFAULT_VALUE: 0.0287,
        CodePattern.DICT_COMPREHENSION: 0.0287,
        CodePattern.IF_TYPE_CHECK: 0.0230,
        CodePattern.RETURN_DICT: 0.0172,
        CodePattern.IF_NOT_NONE: 0.0172,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_TRANSFORM): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3387,
        CodePattern.DICT_GET_DEFAULT: 0.3065,
        CodePattern.CONTEXT_MANAGER: 0.1129,
        CodePattern.INIT_DEFAULT_VALUE: 0.0968,
        CodePattern.STRING_FORMAT: 0.0484,
        CodePattern.GUARD_CLAUSE: 0.0484,
        CodePattern.IF_EMPTY_CHECK: 0.0484,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3750,
        CodePattern.RETURN_COMPUTED: 0.1528,
        CodePattern.IF_NOT_NONE: 0.0694,
        CodePattern.IF_NONE_CHECK: 0.0694,
        CodePattern.IF_EMPTY_CHECK: 0.0509,
        CodePattern.INIT_METHOD: 0.0463,
        CodePattern.PROPERTY_GETTER: 0.0417,
        CodePattern.UNPACKING: 0.0370,
        CodePattern.IF_TYPE_CHECK: 0.0370,
        CodePattern.GUARD_CLAUSE: 0.0231,
        CodePattern.TERNARY_EXPRESSION: 0.0231,
        CodePattern.INIT_DEFAULT_VALUE: 0.0185,
        CodePattern.CONTEXT_MANAGER: 0.0139,
        CodePattern.DICT_GET_DEFAULT: 0.0139,
        CodePattern.GENERATOR_EXPRESSION: 0.0139,
        CodePattern.LOOP_DICT_ITEMS: 0.0139,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4393,
        CodePattern.FUNCTION_TRANSFORMER: 0.0982,
        CodePattern.IF_EMPTY_CHECK: 0.0724,
        CodePattern.UNPACKING: 0.0646,
        CodePattern.INIT_DEFAULT_VALUE: 0.0413,
        CodePattern.GUARD_CLAUSE: 0.0362,
        CodePattern.RETURN_LIST: 0.0336,
        CodePattern.IF_TYPE_CHECK: 0.0336,
        CodePattern.INIT_EMPTY_LIST: 0.0284,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0207,
        CodePattern.CONTEXT_MANAGER: 0.0181,
        CodePattern.DICT_GET_DEFAULT: 0.0181,
        CodePattern.IF_NONE_CHECK: 0.0155,
        CodePattern.LIST_COMPREHENSION: 0.0129,
        CodePattern.TERNARY_EXPRESSION: 0.0129,
        CodePattern.IF_NOT_NONE: 0.0129,
        CodePattern.RETURN_DICT: 0.0103,
        CodePattern.RETURN_NONE: 0.0078,
        CodePattern.LOOP_ACCUMULATE: 0.0078,
        CodePattern.RETURN_BOOL: 0.0078,
        CodePattern.STRING_FORMAT: 0.0078,
    },
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5652,
        CodePattern.RETURN_COMPUTED: 0.2609,
        CodePattern.RETURN_NONE: 0.1739,
    },
    (CodePattern.CLASS_METHOD, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.RETURN_COMPUTED): {
        CodePattern.RETURN_COMPUTED: 0.7170,
        CodePattern.FUNCTION_TRANSFORMER: 0.1509,
        CodePattern.INIT_METHOD: 0.0566,
        CodePattern.RETURN_NONE: 0.0472,
        CodePattern.RETURN_LIST: 0.0283,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.CONTEXT_MANAGER: 0.4884,
        CodePattern.GENERATOR_EXPRESSION: 0.2093,
        CodePattern.INIT_DEFAULT_VALUE: 0.1395,
        CodePattern.FUNCTION_TRANSFORMER: 0.0930,
        CodePattern.LIST_COMPREHENSION: 0.0698,
    },
    (CodePattern.UNPACKING, CodePattern.TRY_FINALLY): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7593,
        CodePattern.CONTEXT_MANAGER: 0.1111,
        CodePattern.INIT_METHOD: 0.0741,
        CodePattern.DICT_GET_DEFAULT: 0.0556,
    },
    (CodePattern.RETURN_NONE, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.7273,
        CodePattern.RETURN_COMPUTED: 0.2727,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.2634,
        CodePattern.FUNCTION_TRANSFORMER: 0.2043,
        CodePattern.CONTEXT_MANAGER: 0.1828,
        CodePattern.RETURN_COMPUTED: 0.1022,
        CodePattern.INIT_METHOD: 0.0430,
        CodePattern.INIT_COUNTER: 0.0376,
        CodePattern.LOOP_ACCUMULATE: 0.0376,
        CodePattern.INIT_EMPTY_LIST: 0.0323,
        CodePattern.IF_EMPTY_CHECK: 0.0323,
        CodePattern.GUARD_CLAUSE: 0.0323,
        CodePattern.STRING_FORMAT: 0.0323,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_DICT): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7808,
        CodePattern.INIT_DEFAULT_VALUE: 0.0959,
        CodePattern.STRING_FORMAT: 0.0685,
        CodePattern.TERNARY_EXPRESSION: 0.0548,
    },
    (CodePattern.RETURN_DICT, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5000,
        CodePattern.INIT_DEFAULT_VALUE: 0.5000,
    },
    (CodePattern.RETURN_NONE, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5361,
        CodePattern.RETURN_COMPUTED: 0.1134,
        CodePattern.INIT_DEFAULT_VALUE: 0.0928,
        CodePattern.STRING_FORMAT: 0.0619,
        CodePattern.INIT_METHOD: 0.0619,
        CodePattern.LOOP_ACCUMULATE: 0.0412,
        CodePattern.IF_EMPTY_CHECK: 0.0309,
        CodePattern.CLASS_METHOD: 0.0309,
        CodePattern.TRY_EXCEPT_PASS: 0.0309,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.7500,
        CodePattern.IF_EMPTY_CHECK: 0.2500,
    },
    (CodePattern.LOGGING_CALL, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.3210,
        CodePattern.LOGGING_CALL: 0.2840,
        CodePattern.CONTEXT_MANAGER: 0.2469,
        CodePattern.DICT_GET_DEFAULT: 0.0988,
        CodePattern.FUNCTION_TRANSFORMER: 0.0494,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.STRING_FORMAT): {
        CodePattern.DICT_GET_DEFAULT: 0.4400,
        CodePattern.CONTEXT_MANAGER: 0.2800,
        CodePattern.STRING_FORMAT: 0.1600,
        CodePattern.LOGGING_CALL: 0.1200,
    },
    (CodePattern.STRING_FORMAT, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.5000,
        CodePattern.INIT_DEFAULT_VALUE: 0.3125,
        CodePattern.CONTEXT_MANAGER: 0.1875,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 0.3538,
        CodePattern.UNPACKING: 0.2615,
        CodePattern.CONTEXT_MANAGER: 0.1077,
        CodePattern.FUNCTION_TRANSFORMER: 0.0923,
        CodePattern.RETURN_COMPUTED: 0.0769,
        CodePattern.GENERATOR_EXPRESSION: 0.0615,
        CodePattern.INIT_DEFAULT_VALUE: 0.0462,
    },
    (CodePattern.STRING_FORMAT, CodePattern.UNPACKING): {
        CodePattern.STRING_FORMAT: 0.5370,
        CodePattern.UNPACKING: 0.2222,
        CodePattern.CONTEXT_MANAGER: 0.1296,
        CodePattern.INIT_DEFAULT_VALUE: 0.0556,
        CodePattern.LOOP_ACCUMULATE: 0.0556,
    },
    (CodePattern.INIT_METHOD, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.4091,
        CodePattern.STRING_FORMAT: 0.1818,
        CodePattern.INIT_EMPTY_LIST: 0.1364,
        CodePattern.LOOP_ACCUMULATE: 0.1364,
        CodePattern.LOOP_TRANSFORM: 0.1364,
    },
    (CodePattern.UNPACKING, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.UNPACKING: 0.3636,
        CodePattern.LOOP_TRANSFORM: 0.1818,
        CodePattern.INIT_EMPTY_LIST: 0.1818,
        CodePattern.INIT_DEFAULT_VALUE: 0.1364,
        CodePattern.LOOP_FILTER: 0.1364,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_ENUMERATE): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_NONE_CHECK): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4091,
        CodePattern.RETURN_COMPUTED: 0.1818,
        CodePattern.CONTEXT_MANAGER: 0.1364,
        CodePattern.IF_NONE_CHECK: 0.1364,
        CodePattern.TRY_EXCEPT_PASS: 0.1364,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.2703,
        CodePattern.RETURN_NONE: 0.1892,
        CodePattern.INIT_DEFAULT_VALUE: 0.1081,
        CodePattern.IF_NONE_CHECK: 0.1081,
        CodePattern.IF_EMPTY_CHECK: 0.1081,
        CodePattern.INIT_EMPTY_DICT: 0.1081,
        CodePattern.FUNCTION_TRANSFORMER: 0.1081,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.STRING_FORMAT): {
        CodePattern.GENERATOR_EXPRESSION: 0.2727,
        CodePattern.FUNCTION_TRANSFORMER: 0.2273,
        CodePattern.STRING_FORMAT: 0.1591,
        CodePattern.INIT_DEFAULT_VALUE: 0.1136,
        CodePattern.LIST_COMPREHENSION: 0.0909,
        CodePattern.INIT_EMPTY_LIST: 0.0682,
        CodePattern.IF_EMPTY_CHECK: 0.0682,
    },
    (CodePattern.UNPACKING, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.2624,
        CodePattern.FUNCTION_TRANSFORMER: 0.1844,
        CodePattern.UNPACKING: 0.1631,
        CodePattern.GUARD_CLAUSE: 0.1135,
        CodePattern.INIT_EMPTY_LIST: 0.0496,
        CodePattern.IF_NONE_CHECK: 0.0496,
        CodePattern.IF_EMPTY_CHECK: 0.0426,
        CodePattern.RETURN_LIST: 0.0284,
        CodePattern.RETURN_BOOL: 0.0213,
        CodePattern.TERNARY_EXPRESSION: 0.0213,
        CodePattern.LIST_COMPREHENSION: 0.0213,
        CodePattern.IF_TYPE_CHECK: 0.0213,
        CodePattern.FUNCTION_VALIDATOR: 0.0213,
    },
    (CodePattern.RETURN_NONE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.2600,
        CodePattern.RETURN_NONE: 0.1600,
        CodePattern.IF_EMPTY_CHECK: 0.1400,
        CodePattern.GUARD_CLAUSE: 0.1200,
        CodePattern.FUNCTION_TRANSFORMER: 0.0900,
        CodePattern.IF_NONE_CHECK: 0.0700,
        CodePattern.IF_NOT_NONE: 0.0400,
        CodePattern.UNPACKING: 0.0300,
        CodePattern.RETURN_BOOL: 0.0300,
        CodePattern.RETURN_LIST: 0.0300,
        CodePattern.INIT_EMPTY_LIST: 0.0300,
    },
    (CodePattern.LOGGING_CALL, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4699,
        CodePattern.FUNCTION_TRANSFORMER: 0.1446,
        CodePattern.GUARD_CLAUSE: 0.0964,
        CodePattern.IF_EMPTY_CHECK: 0.0602,
        CodePattern.INIT_EMPTY_LIST: 0.0482,
        CodePattern.IF_NOT_NONE: 0.0361,
        CodePattern.LOGGING_CALL: 0.0361,
        CodePattern.CONTEXT_MANAGER: 0.0361,
        CodePattern.RETURN_DICT: 0.0361,
        CodePattern.UNPACKING: 0.0361,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.FUNCTION_TRANSFORMER: 0.1714,
        CodePattern.DICT_GET_DEFAULT: 0.0857,
        CodePattern.STRING_FORMAT: 0.0857,
        CodePattern.INIT_DEFAULT_VALUE: 0.0857,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.LOOP_DICT_ITEMS: 0.2353,
        CodePattern.IF_NONE_CHECK: 0.2353,
        CodePattern.INIT_EMPTY_LIST: 0.1765,
        CodePattern.IF_NOT_NONE: 0.1765,
        CodePattern.RETURN_COMPUTED: 0.1765,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 0.4545,
        CodePattern.INIT_DEFAULT_VALUE: 0.3864,
        CodePattern.FUNCTION_TRANSFORMER: 0.0909,
        CodePattern.IF_EMPTY_CHECK: 0.0682,
    },
    (CodePattern.LOGGING_CALL, CodePattern.CLASS_METHOD): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5667,
        CodePattern.INIT_EMPTY_LIST: 0.1333,
        CodePattern.CONTEXT_MANAGER: 0.1000,
        CodePattern.LOOP_FILTER: 0.1000,
        CodePattern.INIT_COUNTER: 0.1000,
    },
    (CodePattern.INIT_METHOD, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_DICT: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.DICT_COMPREHENSION): {
        CodePattern.CONTEXT_MANAGER: 0.5000,
        CodePattern.DICT_GET_DEFAULT: 0.5000,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.IF_TYPE_CHECK: 0.6250,
        CodePattern.IF_EMPTY_CHECK: 0.3750,
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6429,
        CodePattern.RETURN_COMPUTED: 0.3571,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6047,
        CodePattern.RETURN_COMPUTED: 0.0698,
        CodePattern.CONTEXT_MANAGER: 0.0465,
        CodePattern.FUNCTION_VALIDATOR: 0.0388,
        CodePattern.PROPERTY_GETTER: 0.0388,
        CodePattern.INIT_DEFAULT_VALUE: 0.0310,
        CodePattern.INIT_COUNTER: 0.0310,
        CodePattern.GENERATOR_EXPRESSION: 0.0233,
        CodePattern.TERNARY_EXPRESSION: 0.0233,
        CodePattern.IF_NONE_CHECK: 0.0233,
        CodePattern.LIST_COMPREHENSION: 0.0233,
        CodePattern.DICT_COMPREHENSION: 0.0233,
        CodePattern.STRING_FORMAT: 0.0233,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.GENERATOR_EXPRESSION: 0.4667,
        CodePattern.CONTEXT_MANAGER: 0.2667,
        CodePattern.LIST_COMPREHENSION: 0.2667,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_NONE): {
        CodePattern.RETURN_COMPUTED: 0.1923,
        CodePattern.IF_EMPTY_CHECK: 0.1154,
        CodePattern.GUARD_CLAUSE: 0.1058,
        CodePattern.FUNCTION_TRANSFORMER: 0.0865,
        CodePattern.UNPACKING: 0.0769,
        CodePattern.CONTEXT_MANAGER: 0.0577,
        CodePattern.LIST_COMPREHENSION: 0.0577,
        CodePattern.IF_TYPE_CHECK: 0.0481,
        CodePattern.LOGGING_CALL: 0.0481,
        CodePattern.IF_NONE_CHECK: 0.0481,
        CodePattern.LOOP_ACCUMULATE: 0.0385,
        CodePattern.INIT_COUNTER: 0.0385,
        CodePattern.DICT_GET_DEFAULT: 0.0288,
        CodePattern.GENERATOR_EXPRESSION: 0.0288,
        CodePattern.RETURN_NONE: 0.0288,
    },
    (CodePattern.RETURN_NONE, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.7273,
        CodePattern.LIST_COMPREHENSION: 0.2727,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4000,
        CodePattern.CONTEXT_MANAGER: 0.3667,
        CodePattern.INIT_COUNTER: 0.1333,
        CodePattern.FUNCTION_TRANSFORMER: 0.1000,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.INIT_DEFAULT_VALUE: 0.3000,
        CodePattern.CONTEXT_MANAGER: 0.2750,
        CodePattern.DICT_GET_DEFAULT: 0.1250,
        CodePattern.RETURN_COMPUTED: 0.1250,
        CodePattern.IF_EMPTY_CHECK: 0.1000,
        CodePattern.TERNARY_EXPRESSION: 0.0750,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.TRY_FINALLY): {
        CodePattern.DICT_GET_DEFAULT: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4231,
        CodePattern.TERNARY_EXPRESSION: 0.2308,
        CodePattern.INIT_DEFAULT_VALUE: 0.1923,
        CodePattern.IF_EMPTY_CHECK: 0.1538,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_COUNTER): {
        CodePattern.LOOP_ACCUMULATE: 0.2571,
        CodePattern.INIT_DEFAULT_VALUE: 0.2000,
        CodePattern.FUNCTION_TRANSFORMER: 0.1714,
        CodePattern.INIT_EMPTY_LIST: 0.1143,
        CodePattern.RETURN_COMPUTED: 0.0857,
        CodePattern.INIT_COUNTER: 0.0857,
        CodePattern.IF_EMPTY_CHECK: 0.0857,
    },
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.7143,
        CodePattern.RETURN_COMPUTED: 0.1429,
        CodePattern.INIT_DEFAULT_VALUE: 0.1429,
    },
    (CodePattern.INIT_METHOD, CodePattern.CLASS_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.LIST_COMPREHENSION: 1.0000
    },
    (CodePattern.INIT_COUNTER, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5385,
        CodePattern.RETURN_COMPUTED: 0.2308,
        CodePattern.CLASS_METHOD: 0.2308,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_COUNTER: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4359,
        CodePattern.RETURN_COMPUTED: 0.2308,
        CodePattern.INIT_METHOD: 0.0897,
        CodePattern.INIT_DEFAULT_VALUE: 0.0769,
        CodePattern.STRING_FORMAT: 0.0641,
        CodePattern.PROPERTY_GETTER: 0.0641,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0385,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.8031,
        CodePattern.IF_TYPE_CHECK: 0.0551,
        CodePattern.LOOP_ACCUMULATE: 0.0472,
        CodePattern.UNPACKING: 0.0394,
        CodePattern.GUARD_CLAUSE: 0.0315,
        CodePattern.FUNCTION_TRANSFORMER: 0.0236,
    },
    (CodePattern.RETURN_NONE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_NONE: 0.3750,
        CodePattern.FUNCTION_TRANSFORMER: 0.2917,
        CodePattern.RETURN_COMPUTED: 0.2083,
        CodePattern.GUARD_CLAUSE: 0.1250,
    },
    (CodePattern.RETURN_NONE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.8590,
        CodePattern.FUNCTION_VALIDATOR: 0.0641,
        CodePattern.RETURN_COMPUTED: 0.0385,
        CodePattern.RETURN_NONE: 0.0385,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 0.5455,
        CodePattern.IF_EMPTY_CHECK: 0.2386,
        CodePattern.IF_NONE_CHECK: 0.1250,
        CodePattern.IF_TYPE_CHECK: 0.0568,
        CodePattern.UNPACKING: 0.0341,
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_NONE: 0.4722,
        CodePattern.RETURN_COMPUTED: 0.2222,
        CodePattern.RETURN_BOOL: 0.1667,
        CodePattern.RETURN_LIST: 0.1389,
    },
    (CodePattern.RETURN_NONE, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5556,
        CodePattern.IF_TYPE_CHECK: 0.2778,
        CodePattern.GUARD_CLAUSE: 0.1667,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_NONE): {
        CodePattern.RETURN_COMPUTED: 0.5059,
        CodePattern.GUARD_CLAUSE: 0.0941,
        CodePattern.UNPACKING: 0.0824,
        CodePattern.FUNCTION_TRANSFORMER: 0.0706,
        CodePattern.IF_TYPE_CHECK: 0.0706,
        CodePattern.IF_EMPTY_CHECK: 0.0588,
        CodePattern.TRY_EXCEPT_PASS: 0.0471,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0353,
        CodePattern.TERNARY_EXPRESSION: 0.0353,
    },
    (CodePattern.RETURN_BOOL, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3085,
        CodePattern.RETURN_BOOL: 0.2340,
        CodePattern.GUARD_CLAUSE: 0.1596,
        CodePattern.FUNCTION_TRANSFORMER: 0.1383,
        CodePattern.IF_EMPTY_CHECK: 0.0745,
        CodePattern.CONTEXT_MANAGER: 0.0532,
        CodePattern.DICT_GET_DEFAULT: 0.0319,
    },
    (CodePattern.RETURN_BOOL, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.3333,
        CodePattern.FUNCTION_TRANSFORMER: 0.3333,
        CodePattern.INIT_DEFAULT_VALUE: 0.3333,
    },
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6000,
        CodePattern.GENERATOR_EXPRESSION: 0.1750,
        CodePattern.RETURN_COMPUTED: 0.1250,
        CodePattern.INIT_METHOD: 0.1000,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.RETURN_COMPUTED: 0.1765,
        CodePattern.LOOP_DICT_ITEMS: 0.1373,
        CodePattern.IF_NOT_NONE: 0.1176,
        CodePattern.INIT_EMPTY_DICT: 0.1176,
        CodePattern.INIT_EMPTY_LIST: 0.0784,
        CodePattern.LOOP_FILTER: 0.0784,
        CodePattern.CONTEXT_MANAGER: 0.0588,
        CodePattern.TERNARY_EXPRESSION: 0.0588,
        CodePattern.TRY_EXCEPT_PASS: 0.0588,
        CodePattern.DICT_COMPREHENSION: 0.0588,
        CodePattern.IF_EMPTY_CHECK: 0.0588,
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.INIT_EMPTY_DICT: 0.4737,
        CodePattern.LOOP_DICT_ITEMS: 0.2105,
        CodePattern.INIT_METHOD: 0.1579,
        CodePattern.INIT_DEFAULT_VALUE: 0.1579,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 0.5961,
        CodePattern.PROPERTY_GETTER: 0.0784,
        CodePattern.GUARD_CLAUSE: 0.0784,
        CodePattern.IF_EMPTY_CHECK: 0.0667,
        CodePattern.FUNCTION_TRANSFORMER: 0.0627,
        CodePattern.TERNARY_EXPRESSION: 0.0275,
        CodePattern.UNPACKING: 0.0235,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0196,
        CodePattern.INIT_METHOD: 0.0118,
        CodePattern.INIT_DEFAULT_VALUE: 0.0118,
        CodePattern.LIST_COMPREHENSION: 0.0118,
        CodePattern.IF_NONE_CHECK: 0.0118,
    },
    (CodePattern.RETURN_DICT, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3623,
        CodePattern.RETURN_DICT: 0.3623,
        CodePattern.FUNCTION_TRANSFORMER: 0.1014,
        CodePattern.INIT_DEFAULT_VALUE: 0.0870,
        CodePattern.GUARD_CLAUSE: 0.0435,
        CodePattern.RETURN_NONE: 0.0435,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.IF_NONE_CHECK): {
        CodePattern.INIT_EMPTY_LIST: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.8000,
        CodePattern.RETURN_NONE: 0.2000,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_COMPUTED): {
        CodePattern.RETURN_COMPUTED: 0.3285,
        CodePattern.GUARD_CLAUSE: 0.1490,
        CodePattern.FUNCTION_TRANSFORMER: 0.1474,
        CodePattern.STRING_FORMAT: 0.0353,
        CodePattern.IF_EMPTY_CHECK: 0.0353,
        CodePattern.RETURN_NONE: 0.0337,
        CodePattern.INIT_DEFAULT_VALUE: 0.0240,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0240,
        CodePattern.PROPERTY_GETTER: 0.0208,
        CodePattern.INIT_METHOD: 0.0192,
        CodePattern.IF_TYPE_CHECK: 0.0176,
        CodePattern.CONTEXT_MANAGER: 0.0160,
        CodePattern.RETURN_BOOL: 0.0160,
        CodePattern.UNPACKING: 0.0144,
        CodePattern.DICT_GET_DEFAULT: 0.0128,
        CodePattern.LIST_COMPREHENSION: 0.0128,
        CodePattern.IF_NONE_CHECK: 0.0112,
        CodePattern.LOOP_ACCUMULATE: 0.0112,
        CodePattern.RETURN_LIST: 0.0096,
        CodePattern.INIT_EMPTY_LIST: 0.0096,
        CodePattern.TERNARY_EXPRESSION: 0.0096,
        CodePattern.LOGGING_CALL: 0.0080,
        CodePattern.TRY_EXCEPT_PASS: 0.0080,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0080,
        CodePattern.GENERATOR_EXPRESSION: 0.0064,
        CodePattern.IF_NOT_NONE: 0.0064,
        CodePattern.CLASS_METHOD: 0.0048,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.6667,
        CodePattern.INIT_EMPTY_LIST: 0.3333,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.4590,
        CodePattern.RETURN_NONE: 0.1557,
        CodePattern.RETURN_LIST: 0.1189,
        CodePattern.RETURN_BOOL: 0.0799,
        CodePattern.GUARD_CLAUSE: 0.0369,
        CodePattern.FUNCTION_TRANSFORMER: 0.0348,
        CodePattern.UNPACKING: 0.0225,
        CodePattern.RETURN_DICT: 0.0164,
        CodePattern.INIT_DEFAULT_VALUE: 0.0164,
        CodePattern.GENERATOR_EXPRESSION: 0.0123,
        CodePattern.TERNARY_EXPRESSION: 0.0102,
        CodePattern.LIST_COMPREHENSION: 0.0102,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0082,
        CodePattern.LOGGING_CALL: 0.0061,
        CodePattern.IF_EMPTY_CHECK: 0.0061,
        CodePattern.LOOP_DICT_ITEMS: 0.0061,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_BOOL): {
        CodePattern.RETURN_BOOL: 0.3363,
        CodePattern.GUARD_CLAUSE: 0.2920,
        CodePattern.RETURN_COMPUTED: 0.2301,
        CodePattern.FUNCTION_TRANSFORMER: 0.0442,
        CodePattern.IF_EMPTY_CHECK: 0.0354,
        CodePattern.IF_NONE_CHECK: 0.0354,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0265,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.RETURN_COMPUTED: 0.3750,
        CodePattern.GUARD_CLAUSE: 0.1500,
        CodePattern.DICT_GET_DEFAULT: 0.1375,
        CodePattern.FUNCTION_TRANSFORMER: 0.0875,
        CodePattern.IF_NOT_NONE: 0.0750,
        CodePattern.IF_NONE_CHECK: 0.0750,
        CodePattern.TERNARY_EXPRESSION: 0.0625,
        CodePattern.INIT_DEFAULT_VALUE: 0.0375,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.8529,
        CodePattern.INIT_DEFAULT_VALUE: 0.1471,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 0.4444,
        CodePattern.IF_NONE_CHECK: 0.3333,
        CodePattern.IF_EMPTY_CHECK: 0.2222,
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.3295,
        CodePattern.RETURN_NONE: 0.2159,
        CodePattern.GUARD_CLAUSE: 0.1932,
        CodePattern.RETURN_BOOL: 0.1818,
        CodePattern.RETURN_LIST: 0.0795,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.GUARD_CLAUSE): {
        CodePattern.GUARD_CLAUSE: 0.4103,
        CodePattern.RETURN_COMPUTED: 0.2564,
        CodePattern.FUNCTION_TRANSFORMER: 0.1410,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0385,
        CodePattern.LOOP_ACCUMULATE: 0.0385,
        CodePattern.UNPACKING: 0.0385,
        CodePattern.IF_EMPTY_CHECK: 0.0385,
        CodePattern.RETURN_NONE: 0.0385,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.2703,
        CodePattern.GUARD_CLAUSE: 0.1892,
        CodePattern.FUNCTION_TRANSFORMER: 0.1892,
        CodePattern.UNPACKING: 0.1892,
        CodePattern.TERNARY_EXPRESSION: 0.0811,
        CodePattern.IF_NONE_CHECK: 0.0811,
    },
    (CodePattern.STRING_FORMAT, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_COUNTER: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.4434,
        CodePattern.LOGGING_CALL: 0.3538,
        CodePattern.CONTEXT_MANAGER: 0.1038,
        CodePattern.INIT_DEFAULT_VALUE: 0.0377,
        CodePattern.CLASS_METHOD: 0.0330,
        CodePattern.LIST_COMPREHENSION: 0.0142,
        CodePattern.STRING_FORMAT: 0.0142,
    },
    (CodePattern.STRING_FORMAT, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.STRING_FORMAT: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.TRY_FINALLY, CodePattern.LIST_COMPREHENSION): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.2745,
        CodePattern.RETURN_COMPUTED: 0.1961,
        CodePattern.IF_EMPTY_CHECK: 0.1373,
        CodePattern.FUNCTION_TRANSFORMER: 0.0980,
        CodePattern.GUARD_CLAUSE: 0.0980,
        CodePattern.IF_NOT_NONE: 0.0784,
        CodePattern.INIT_METHOD: 0.0588,
        CodePattern.LIST_COMPREHENSION: 0.0588,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_FINALLY): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.UNPACKING): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7368,
        CodePattern.UNPACKING: 0.2632,
    },
    (CodePattern.INIT_COUNTER, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3571,
        CodePattern.IF_NONE_CHECK: 0.1429,
        CodePattern.IF_EMPTY_CHECK: 0.1429,
        CodePattern.UNPACKING: 0.1190,
        CodePattern.PROPERTY_GETTER: 0.0952,
        CodePattern.IF_NOT_NONE: 0.0714,
        CodePattern.TERNARY_EXPRESSION: 0.0714,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3750,
        CodePattern.UNPACKING: 0.2083,
        CodePattern.GUARD_CLAUSE: 0.1667,
        CodePattern.FUNCTION_TRANSFORMER: 0.1250,
        CodePattern.IF_NONE_CHECK: 0.1250,
    },
    (CodePattern.INIT_METHOD, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 0.2059,
        CodePattern.CONTEXT_MANAGER: 0.1765,
        CodePattern.STRING_FORMAT: 0.1765,
        CodePattern.GENERATOR_EXPRESSION: 0.1471,
        CodePattern.TERNARY_EXPRESSION: 0.1176,
        CodePattern.INIT_DEFAULT_VALUE: 0.0882,
        CodePattern.FUNCTION_TRANSFORMER: 0.0882,
    },
    (CodePattern.CLASS_METHOD, CodePattern.LOGGING_CALL): {
        CodePattern.DICT_GET_DEFAULT: 0.5882,
        CodePattern.LOGGING_CALL: 0.1569,
        CodePattern.CONTEXT_MANAGER: 0.1176,
        CodePattern.CLASS_METHOD: 0.0784,
        CodePattern.INIT_DEFAULT_VALUE: 0.0588,
    },
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.LOGGING_CALL): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5745,
        CodePattern.PROPERTY_GETTER: 0.1489,
        CodePattern.LOGGING_CALL: 0.1277,
        CodePattern.IF_EMPTY_CHECK: 0.0851,
        CodePattern.RETURN_COMPUTED: 0.0638,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6667,
        CodePattern.STRING_FORMAT: 0.1296,
        CodePattern.RETURN_COMPUTED: 0.0926,
        CodePattern.INIT_DEFAULT_VALUE: 0.0556,
        CodePattern.IF_EMPTY_CHECK: 0.0556,
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.RETURN_BOOL: 0.4286,
    },
    (CodePattern.RETURN_LIST, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_LIST: 0.6395,
        CodePattern.GUARD_CLAUSE: 0.1163,
        CodePattern.IF_EMPTY_CHECK: 0.0698,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0581,
        CodePattern.FUNCTION_TRANSFORMER: 0.0465,
        CodePattern.IF_NOT_NONE: 0.0349,
        CodePattern.STRING_FORMAT: 0.0349,
    },
    (CodePattern.UNPACKING, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.4600,
        CodePattern.UNPACKING: 0.3200,
        CodePattern.INIT_DEFAULT_VALUE: 0.1000,
        CodePattern.IF_EMPTY_CHECK: 0.0600,
        CodePattern.FUNCTION_TRANSFORMER: 0.0600,
    },
    (CodePattern.UNPACKING, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6667,
        CodePattern.UNPACKING: 0.3333,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3741,
        CodePattern.RETURN_COMPUTED: 0.2857,
        CodePattern.INIT_DEFAULT_VALUE: 0.0544,
        CodePattern.TERNARY_EXPRESSION: 0.0476,
        CodePattern.GUARD_CLAUSE: 0.0408,
        CodePattern.STRING_FORMAT: 0.0340,
        CodePattern.DICT_COMPREHENSION: 0.0340,
        CodePattern.LIST_COMPREHENSION: 0.0272,
        CodePattern.LOOP_ACCUMULATE: 0.0204,
        CodePattern.INIT_EMPTY_LIST: 0.0204,
        CodePattern.UNPACKING: 0.0204,
        CodePattern.GENERATOR_EXPRESSION: 0.0204,
        CodePattern.RETURN_DICT: 0.0204,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.UNPACKING): {
        CodePattern.LIST_COMPREHENSION: 0.5000,
        CodePattern.UNPACKING: 0.2857,
        CodePattern.CONTEXT_MANAGER: 0.2143,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_ENUMERATE): {
        CodePattern.IF_EMPTY_CHECK: 0.3636,
        CodePattern.RETURN_COMPUTED: 0.3636,
        CodePattern.IF_TYPE_CHECK: 0.2727,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.1863,
        CodePattern.INIT_DEFAULT_VALUE: 0.0686,
        CodePattern.INIT_METHOD: 0.0490,
        CodePattern.IF_NOT_NONE: 0.0490,
        CodePattern.PROPERTY_GETTER: 0.0392,
        CodePattern.RETURN_NONE: 0.0392,
        CodePattern.IF_NONE_CHECK: 0.0392,
        CodePattern.IF_TYPE_CHECK: 0.0294,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.IF_EMPTY_CHECK: 0.5000,
        CodePattern.FUNCTION_TRANSFORMER: 0.5000,
    },
    (CodePattern.RETURN_NONE, CodePattern.RETURN_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.8545,
        CodePattern.RETURN_BOOL: 0.0545,
        CodePattern.RETURN_NONE: 0.0485,
        CodePattern.IF_TYPE_CHECK: 0.0242,
        CodePattern.RETURN_LIST: 0.0182,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 0.7125,
        CodePattern.RETURN_LIST: 0.1375,
        CodePattern.FUNCTION_TRANSFORMER: 0.0375,
        CodePattern.RETURN_NONE: 0.0375,
        CodePattern.IF_EMPTY_CHECK: 0.0375,
        CodePattern.UNPACKING: 0.0375,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.FUNCTION_TRANSFORMER: 0.4286,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LOOP_ZIP): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOOP_ZIP): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOOP_ENUMERATE): {
        CodePattern.DICT_GET_DEFAULT: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_LIST): {
        CodePattern.RETURN_LIST: 0.2476,
        CodePattern.LOGGING_CALL: 0.2381,
        CodePattern.GUARD_CLAUSE: 0.1905,
        CodePattern.RETURN_COMPUTED: 0.1238,
        CodePattern.INIT_EMPTY_LIST: 0.1048,
        CodePattern.IF_EMPTY_CHECK: 0.0381,
        CodePattern.UNPACKING: 0.0286,
        CodePattern.FUNCTION_TRANSFORMER: 0.0286,
    },
    (CodePattern.RETURN_LIST, CodePattern.RETURN_LIST): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4118,
        CodePattern.LOGGING_CALL: 0.2941,
        CodePattern.INIT_METHOD: 0.1176,
        CodePattern.RETURN_LIST: 0.0882,
        CodePattern.CONTEXT_MANAGER: 0.0882,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NONE_CHECK): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5000,
        CodePattern.IF_NOT_NONE: 0.5000,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.RETURN_COMPUTED): {
        CodePattern.PROPERTY_GETTER: 0.5312,
        CodePattern.FUNCTION_TRANSFORMER: 0.2143,
        CodePattern.INIT_METHOD: 0.0670,
        CodePattern.GENERATOR_EXPRESSION: 0.0536,
        CodePattern.LOGGING_CALL: 0.0312,
        CodePattern.STRING_FORMAT: 0.0268,
        CodePattern.INIT_DEFAULT_VALUE: 0.0223,
        CodePattern.TERNARY_EXPRESSION: 0.0223,
        CodePattern.FUNCTION_VALIDATOR: 0.0179,
        CodePattern.UNPACKING: 0.0134,
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.7222,
        CodePattern.LOOP_DICT_ITEMS: 0.2778,
    },
    (CodePattern.INIT_COUNTER, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_COUNTER: 0.4286,
        CodePattern.INIT_DEFAULT_VALUE: 0.3117,
        CodePattern.INIT_METHOD: 0.0844,
        CodePattern.FUNCTION_TRANSFORMER: 0.0584,
        CodePattern.INIT_EMPTY_LIST: 0.0519,
        CodePattern.RETURN_COMPUTED: 0.0260,
        CodePattern.LOOP_ACCUMULATE: 0.0195,
        CodePattern.CONTEXT_MANAGER: 0.0195,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 0.2600,
        CodePattern.LIST_COMPREHENSION: 0.2000,
        CodePattern.TERNARY_EXPRESSION: 0.1400,
        CodePattern.CONTEXT_MANAGER: 0.1400,
        CodePattern.FUNCTION_TRANSFORMER: 0.1000,
        CodePattern.INIT_EMPTY_LIST: 0.1000,
        CodePattern.GENERATOR_EXPRESSION: 0.0600,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_COUNTER): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3421,
        CodePattern.INIT_METHOD: 0.2368,
        CodePattern.INIT_DEFAULT_VALUE: 0.2105,
        CodePattern.INIT_COUNTER: 0.2105,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.6667,
        CodePattern.RETURN_COMPUTED: 0.3333,
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.LOOP_DICT_ITEMS: 0.5000,
        CodePattern.CONTEXT_MANAGER: 0.5000,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.LOOP_DICT_ITEMS: 0.5714,
        CodePattern.LIST_COMPREHENSION: 0.4286,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 0.4545,
        CodePattern.INIT_DEFAULT_VALUE: 0.2727,
        CodePattern.CONTEXT_MANAGER: 0.2727,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOGGING_CALL): {
        CodePattern.DICT_GET_DEFAULT: 0.6772,
        CodePattern.LOGGING_CALL: 0.1772,
        CodePattern.INIT_DEFAULT_VALUE: 0.0759,
        CodePattern.CONTEXT_MANAGER: 0.0506,
        CodePattern.FUNCTION_TRANSFORMER: 0.0190,
    },
    (CodePattern.STRING_FORMAT, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7333,
        CodePattern.INIT_DEFAULT_VALUE: 0.2667,
    },
    (CodePattern.INIT_METHOD, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.LOGGING_CALL): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.TRY_FINALLY): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 0.5325,
        CodePattern.IF_EMPTY_CHECK: 0.1169,
        CodePattern.IF_NOT_NONE: 0.0779,
        CodePattern.CONTEXT_MANAGER: 0.0649,
        CodePattern.LIST_COMPREHENSION: 0.0649,
        CodePattern.FUNCTION_TRANSFORMER: 0.0519,
        CodePattern.GUARD_CLAUSE: 0.0519,
        CodePattern.INIT_DEFAULT_VALUE: 0.0390,
    },
    (CodePattern.RETURN_BOOL, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.STRING_FORMAT): {
        CodePattern.RETURN_COMPUTED: 0.3529,
        CodePattern.LOGGING_CALL: 0.2353,
        CodePattern.GENERATOR_EXPRESSION: 0.2353,
        CodePattern.STRING_FORMAT: 0.1765,
    },
    (CodePattern.STRING_FORMAT, CodePattern.LOGGING_CALL): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.5652,
        CodePattern.FUNCTION_TRANSFORMER: 0.3043,
        CodePattern.GUARD_CLAUSE: 0.1304,
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.INIT_METHOD): {
        CodePattern.INIT_METHOD: 0.5714,
        CodePattern.FUNCTION_TRANSFORMER: 0.3214,
        CodePattern.IF_EMPTY_CHECK: 0.1071,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.UNPACKING): {
        CodePattern.DICT_GET_DEFAULT: 0.5366,
        CodePattern.UNPACKING: 0.3415,
        CodePattern.CONTEXT_MANAGER: 0.1220,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LIST_COMPREHENSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3455,
        CodePattern.RETURN_COMPUTED: 0.1818,
        CodePattern.TERNARY_EXPRESSION: 0.1182,
        CodePattern.LIST_COMPREHENSION: 0.0909,
        CodePattern.STRING_FORMAT: 0.0727,
        CodePattern.IF_EMPTY_CHECK: 0.0545,
        CodePattern.CONTEXT_MANAGER: 0.0364,
        CodePattern.INIT_METHOD: 0.0364,
        CodePattern.INIT_EMPTY_LIST: 0.0364,
        CodePattern.INIT_DEFAULT_VALUE: 0.0273,
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.6000,
        CodePattern.INIT_EMPTY_LIST: 0.2000,
        CodePattern.IF_EMPTY_CHECK: 0.2000,
    },
    (CodePattern.LOOP_FILTER, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.8387,
        CodePattern.STRING_FORMAT: 0.1613,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.STRING_FORMAT): {
        CodePattern.TERNARY_EXPRESSION: 0.3158,
        CodePattern.GENERATOR_EXPRESSION: 0.2105,
        CodePattern.STRING_FORMAT: 0.1579,
        CodePattern.FUNCTION_TRANSFORMER: 0.1579,
        CodePattern.RETURN_COMPUTED: 0.1579,
    },
    (CodePattern.UNPACKING, CodePattern.IF_NOT_NONE): {
        CodePattern.IF_NOT_NONE: 0.2941,
        CodePattern.FUNCTION_TRANSFORMER: 0.2353,
        CodePattern.IF_TYPE_CHECK: 0.1471,
        CodePattern.UNPACKING: 0.1176,
        CodePattern.RETURN_COMPUTED: 0.1176,
        CodePattern.LOOP_ACCUMULATE: 0.0882,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.IF_NOT_NONE): {
        CodePattern.IF_NOT_NONE: 0.5139,
        CodePattern.RETURN_COMPUTED: 0.1667,
        CodePattern.FUNCTION_TRANSFORMER: 0.1667,
        CodePattern.TERNARY_EXPRESSION: 0.0694,
        CodePattern.UNPACKING: 0.0417,
        CodePattern.LOOP_ACCUMULATE: 0.0417,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.UNPACKING): {CodePattern.IF_NOT_NONE: 1.0000},
    (CodePattern.IF_NOT_NONE, CodePattern.CONTEXT_MANAGER): {
        CodePattern.RETURN_COMPUTED: 0.5556,
        CodePattern.CONTEXT_MANAGER: 0.4444,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.IF_NOT_NONE): {
        CodePattern.DICT_GET_DEFAULT: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.5714,
        CodePattern.RETURN_COMPUTED: 0.4286,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.DICT_COMPREHENSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4800,
        CodePattern.RETURN_COMPUTED: 0.2000,
        CodePattern.CONTEXT_MANAGER: 0.1600,
        CodePattern.TERNARY_EXPRESSION: 0.1600,
    },
    (CodePattern.DICT_COMPREHENSION, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 0.5000,
        CodePattern.IF_EMPTY_CHECK: 0.5000,
    },
    (CodePattern.UNPACKING, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.4000,
        CodePattern.RETURN_NONE: 0.2000,
        CodePattern.IF_EMPTY_CHECK: 0.2000,
        CodePattern.FUNCTION_TRANSFORMER: 0.2000,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_DICT): {
        CodePattern.RETURN_COMPUTED: 0.5000,
        CodePattern.FUNCTION_TRANSFORMER: 0.5000,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3333,
        CodePattern.TERNARY_EXPRESSION: 0.2667,
        CodePattern.CONTEXT_MANAGER: 0.2000,
        CodePattern.GENERATOR_EXPRESSION: 0.2000,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_COUNTER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.LOOP_ENUMERATE, CodePattern.LOOP_ENUMERATE): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_ENUMERATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.4000,
        CodePattern.LOOP_ACCUMULATE: 0.3333,
        CodePattern.INIT_DEFAULT_VALUE: 0.2667,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.STRING_FORMAT): {
        CodePattern.GENERATOR_EXPRESSION: 0.6750,
        CodePattern.STRING_FORMAT: 0.1000,
        CodePattern.FUNCTION_TRANSFORMER: 0.0750,
        CodePattern.RETURN_COMPUTED: 0.0750,
        CodePattern.CONTEXT_MANAGER: 0.0750,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.2326,
        CodePattern.INIT_EMPTY_LIST: 0.1860,
        CodePattern.GUARD_CLAUSE: 0.1395,
        CodePattern.UNPACKING: 0.1163,
        CodePattern.FUNCTION_TRANSFORMER: 0.0930,
        CodePattern.LIST_COMPREHENSION: 0.0930,
        CodePattern.IF_NONE_CHECK: 0.0698,
        CodePattern.IF_TYPE_CHECK: 0.0698,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_BOOL, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_BOOL: 0.8200,
        CodePattern.RETURN_COMPUTED: 0.1800,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOOP_TRANSFORM): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 0.6154,
        CodePattern.RETURN_BOOL: 0.3846,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6000,
        CodePattern.STRING_FORMAT: 0.1167,
        CodePattern.RETURN_COMPUTED: 0.0833,
        CodePattern.CONTEXT_MANAGER: 0.0500,
        CodePattern.GENERATOR_EXPRESSION: 0.0500,
        CodePattern.LIST_COMPREHENSION: 0.0500,
        CodePattern.GUARD_CLAUSE: 0.0500,
    },
    (CodePattern.CLASS_METHOD, CodePattern.RETURN_COMPUTED): {
        CodePattern.CLASS_METHOD: 0.7000,
        CodePattern.FUNCTION_TRANSFORMER: 0.3000,
    },
    (CodePattern.INIT_COUNTER, CodePattern.STRING_FORMAT): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 0.6000,
        CodePattern.RETURN_BOOL: 0.4000,
    },
    (CodePattern.INIT_METHOD, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.UNPACKING): {
        CodePattern.RETURN_COMPUTED: 0.5385,
        CodePattern.UNPACKING: 0.4615,
    },
    (CodePattern.INIT_COUNTER, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.INIT_EMPTY_LIST: 0.3529,
        CodePattern.LOOP_FILTER: 0.2941,
        CodePattern.INIT_COUNTER: 0.1765,
        CodePattern.INIT_DEFAULT_VALUE: 0.1765,
    },
    (CodePattern.CLASS_METHOD, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5333,
        CodePattern.CLASS_METHOD: 0.2667,
        CodePattern.RETURN_LIST: 0.2000,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.IF_EMPTY_CHECK: 0.2805,
        CodePattern.RETURN_COMPUTED: 0.1890,
        CodePattern.FUNCTION_TRANSFORMER: 0.1098,
        CodePattern.LOGGING_CALL: 0.0732,
        CodePattern.TERNARY_EXPRESSION: 0.0488,
        CodePattern.GENERATOR_EXPRESSION: 0.0488,
        CodePattern.INIT_DEFAULT_VALUE: 0.0366,
        CodePattern.STRING_FORMAT: 0.0366,
        CodePattern.LIST_COMPREHENSION: 0.0305,
        CodePattern.CONTEXT_MANAGER: 0.0244,
        CodePattern.LOOP_DICT_ITEMS: 0.0244,
        CodePattern.IF_NOT_NONE: 0.0244,
        CodePattern.DICT_GET_DEFAULT: 0.0183,
        CodePattern.GUARD_CLAUSE: 0.0183,
        CodePattern.UNPACKING: 0.0183,
        CodePattern.IF_NONE_CHECK: 0.0183,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.CLASS_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 0.5000,
        CodePattern.IF_NONE_CHECK: 0.5000,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.2727,
        CodePattern.RETURN_COMPUTED: 0.2273,
        CodePattern.IF_EMPTY_CHECK: 0.1818,
        CodePattern.UNPACKING: 0.1818,
        CodePattern.FUNCTION_TRANSFORMER: 0.1364,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_COMPUTED: 0.4545,
        CodePattern.CONTEXT_MANAGER: 0.2727,
        CodePattern.UNPACKING: 0.2727,
    },
    (CodePattern.LOGGING_CALL, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5085,
        CodePattern.CLASS_METHOD: 0.2203,
        CodePattern.RETURN_COMPUTED: 0.1186,
        CodePattern.LOGGING_CALL: 0.1017,
        CodePattern.FUNCTION_VALIDATOR: 0.0508,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_ENUMERATE): {
        CodePattern.LIST_COMPREHENSION: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 1.0000
    },
    (CodePattern.DICT_COMPREHENSION, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3500,
        CodePattern.IF_EMPTY_CHECK: 0.2000,
        CodePattern.LOOP_DICT_ITEMS: 0.1500,
        CodePattern.LIST_COMPREHENSION: 0.1500,
        CodePattern.TERNARY_EXPRESSION: 0.1500,
    },
    (CodePattern.RETURN_NONE, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.5000,
        CodePattern.INIT_DEFAULT_VALUE: 0.5000,
    },
    (CodePattern.RETURN_NONE, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.DICT_GET_DEFAULT: 1.0000
    },
    (CodePattern.LOOP_ZIP, CodePattern.LOOP_ZIP): {
        CodePattern.LOOP_ZIP: 0.4000,
        CodePattern.DICT_GET_DEFAULT: 0.3000,
        CodePattern.CONTEXT_MANAGER: 0.3000,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_BOOL, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.IF_EMPTY_CHECK: 0.4000,
        CodePattern.TERNARY_EXPRESSION: 0.3000,
        CodePattern.RETURN_COMPUTED: 0.3000,
    },
    (CodePattern.UNPACKING, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.4800,
        CodePattern.UNPACKING: 0.1600,
        CodePattern.FUNCTION_TRANSFORMER: 0.1200,
        CodePattern.TERNARY_EXPRESSION: 0.1200,
        CodePattern.STRING_FORMAT: 0.1200,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_NONE: 0.4694,
        CodePattern.RETURN_COMPUTED: 0.4286,
        CodePattern.GUARD_CLAUSE: 0.1020,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LOOP_ZIP): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_TYPE_CHECK): {
        CodePattern.IF_TYPE_CHECK: 0.3766,
        CodePattern.FUNCTION_TRANSFORMER: 0.1558,
        CodePattern.RETURN_COMPUTED: 0.1299,
        CodePattern.IF_EMPTY_CHECK: 0.1169,
        CodePattern.UNPACKING: 0.1039,
        CodePattern.LOOP_ACCUMULATE: 0.0390,
        CodePattern.LOGGING_CALL: 0.0390,
        CodePattern.GENERATOR_EXPRESSION: 0.0390,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3158,
        CodePattern.GUARD_CLAUSE: 0.1579,
        CodePattern.FUNCTION_TRANSFORMER: 0.1316,
        CodePattern.IF_NONE_CHECK: 0.1053,
        CodePattern.TERNARY_EXPRESSION: 0.1053,
        CodePattern.UNPACKING: 0.1053,
        CodePattern.IF_TYPE_CHECK: 0.0789,
    },
    (CodePattern.RETURN_LIST, CodePattern.UNPACKING): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.2500,
        CodePattern.IF_TYPE_CHECK: 0.2500,
        CodePattern.RETURN_COMPUTED: 0.1562,
        CodePattern.FUNCTION_TRANSFORMER: 0.1562,
        CodePattern.IF_NOT_NONE: 0.0938,
        CodePattern.LIST_COMPREHENSION: 0.0938,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_BOOL): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7333,
        CodePattern.RETURN_COMPUTED: 0.2667,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.6316,
        CodePattern.IF_EMPTY_CHECK: 0.2105,
        CodePattern.TERNARY_EXPRESSION: 0.1579,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.7059,
        CodePattern.RETURN_BOOL: 0.2941,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3968,
        CodePattern.TERNARY_EXPRESSION: 0.1905,
        CodePattern.RETURN_COMPUTED: 0.1587,
        CodePattern.PROPERTY_GETTER: 0.1429,
        CodePattern.IF_EMPTY_CHECK: 0.0635,
        CodePattern.INIT_METHOD: 0.0476,
    },
    (CodePattern.DICT_COMPREHENSION, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.8421,
        CodePattern.INIT_METHOD: 0.1579,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.DICT_COMPREHENSION): {
        CodePattern.DICT_COMPREHENSION: 1.0000
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7333,
        CodePattern.CLASS_METHOD: 0.2667,
    },
    (CodePattern.STRING_FORMAT, CodePattern.LOOP_ENUMERATE): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.LOOP_ENUMERATE, CodePattern.STRING_FORMAT): {
        CodePattern.LOOP_ENUMERATE: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.6154,
        CodePattern.GUARD_CLAUSE: 0.1538,
        CodePattern.FUNCTION_TRANSFORMER: 0.1154,
        CodePattern.TERNARY_EXPRESSION: 0.1154,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.DICT_COMPREHENSION, CodePattern.DICT_COMPREHENSION): {
        CodePattern.DICT_COMPREHENSION: 0.6250,
        CodePattern.FUNCTION_TRANSFORMER: 0.3750,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 0.5000,
        CodePattern.FUNCTION_TRANSFORMER: 0.2500,
        CodePattern.GUARD_CLAUSE: 0.2500,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.INIT_DEFAULT_VALUE: 0.6250,
        CodePattern.UNPACKING: 0.3750,
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.UNPACKING: 0.5000,
        CodePattern.TERNARY_EXPRESSION: 0.5000,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.PROPERTY_GETTER): {
        CodePattern.PROPERTY_GETTER: 0.5227,
        CodePattern.RETURN_COMPUTED: 0.4091,
        CodePattern.FUNCTION_TRANSFORMER: 0.0682,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_DICT): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.CLASS_METHOD, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.3913,
        CodePattern.IF_EMPTY_CHECK: 0.1739,
        CodePattern.IF_NOT_NONE: 0.1739,
        CodePattern.UNPACKING: 0.1304,
        CodePattern.FUNCTION_TRANSFORMER: 0.1304,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.RETURN_LIST): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_LIST): {
        CodePattern.LOGGING_CALL: 0.3333,
        CodePattern.INIT_EMPTY_LIST: 0.2308,
        CodePattern.LIST_COMPREHENSION: 0.1282,
        CodePattern.IF_TYPE_CHECK: 0.1282,
        CodePattern.GUARD_CLAUSE: 0.1026,
        CodePattern.RETURN_LIST: 0.0769,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.3684,
        CodePattern.RETURN_COMPUTED: 0.3158,
        CodePattern.FUNCTION_TRANSFORMER: 0.1579,
        CodePattern.STRING_FORMAT: 0.1579,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.UNPACKING: 1.0000
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.UNPACKING): {
        CodePattern.DICT_GET_DEFAULT: 0.5714,
        CodePattern.UNPACKING: 0.4286,
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 0.6667,
        CodePattern.FUNCTION_TRANSFORMER: 0.3333,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NOT_NONE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.RETURN_LIST): {
        CodePattern.FUNCTION_TRANSFORMER: 0.8163,
        CodePattern.LOGGING_CALL: 0.1224,
        CodePattern.CLASS_METHOD: 0.0612,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6522,
        CodePattern.PROPERTY_GETTER: 0.1304,
        CodePattern.IF_TYPE_CHECK: 0.0870,
        CodePattern.INIT_DEFAULT_VALUE: 0.0652,
        CodePattern.INIT_METHOD: 0.0652,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6017,
        CodePattern.INIT_DEFAULT_VALUE: 0.1017,
        CodePattern.STRING_FORMAT: 0.0678,
        CodePattern.RETURN_COMPUTED: 0.0508,
        CodePattern.INIT_METHOD: 0.0508,
        CodePattern.FUNCTION_VALIDATOR: 0.0424,
        CodePattern.LIST_COMPREHENSION: 0.0339,
        CodePattern.TERNARY_EXPRESSION: 0.0254,
        CodePattern.PROPERTY_GETTER: 0.0254,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.STATIC_METHOD, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.LIST_COMPREHENSION): {
        CodePattern.RETURN_COMPUTED: 0.6500,
        CodePattern.TERNARY_EXPRESSION: 0.2000,
        CodePattern.RETURN_LIST: 0.1500,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.6154,
        CodePattern.RETURN_LIST: 0.3846,
    },
    (CodePattern.RETURN_LIST, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.LIST_COMPREHENSION): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.RETURN_LIST): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_TYPE_CHECK): {
        CodePattern.GENERATOR_EXPRESSION: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LIST_COMPREHENSION): {
        CodePattern.IF_EMPTY_CHECK: 0.3333,
        CodePattern.TERNARY_EXPRESSION: 0.2222,
        CodePattern.STRING_FORMAT: 0.1852,
        CodePattern.LIST_COMPREHENSION: 0.1481,
        CodePattern.FUNCTION_TRANSFORMER: 0.1111,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LIST_COMPREHENSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.LIST_COMPREHENSION: 0.2500,
        CodePattern.STRING_FORMAT: 0.2188,
        CodePattern.RETURN_COMPUTED: 0.1875,
        CodePattern.IF_EMPTY_CHECK: 0.1250,
        CodePattern.FUNCTION_TRANSFORMER: 0.1250,
        CodePattern.INIT_EMPTY_LIST: 0.0938,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOOP_DICT_ITEMS): {
        CodePattern.IF_EMPTY_CHECK: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_DICT): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_DICT, CodePattern.STRING_FORMAT): {
        CodePattern.GENERATOR_EXPRESSION: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_COUNTER): {
        CodePattern.LOOP_FILTER: 0.5556,
        CodePattern.LOOP_ACCUMULATE: 0.4444,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 0.6250,
        CodePattern.FUNCTION_TRANSFORMER: 0.3750,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_LIST): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LOOP_ENUMERATE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.LIST_COMPREHENSION): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.IF_NOT_NONE): {
        CodePattern.IF_NOT_NONE: 0.6667,
        CodePattern.RETURN_COMPUTED: 0.3333,
    },
    (CodePattern.RETURN_LIST, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5652,
        CodePattern.INIT_DEFAULT_VALUE: 0.2609,
        CodePattern.INIT_METHOD: 0.1739,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_TYPE_CHECK): {
        CodePattern.IF_TYPE_CHECK: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_NOT_NONE): {
        CodePattern.IF_EMPTY_CHECK: 0.3333,
        CodePattern.RETURN_COMPUTED: 0.2857,
        CodePattern.FUNCTION_TRANSFORMER: 0.2381,
        CodePattern.IF_NOT_NONE: 0.1429,
    },
    (CodePattern.LOOP_ENUMERATE, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6250,
        CodePattern.LOOP_ACCUMULATE: 0.3750,
    },
    (CodePattern.LOOP_FILTER, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_LIST): {
        CodePattern.IF_EMPTY_CHECK: 0.7273,
        CodePattern.INIT_EMPTY_LIST: 0.2727,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.TRY_EXCEPT_RERAISE: 0.5000,
        CodePattern.IF_EMPTY_CHECK: 0.5000,
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7429,
        CodePattern.RETURN_COMPUTED: 0.1000,
        CodePattern.INIT_METHOD: 0.0714,
        CodePattern.INIT_DEFAULT_VALUE: 0.0429,
        CodePattern.CLASS_METHOD: 0.0429,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_FILTER): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.IF_EMPTY_CHECK: 0.4286,
    },
    (CodePattern.LOOP_FILTER, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 0.5714,
        CodePattern.LOGGING_CALL: 0.4286,
    },
    (CodePattern.STRING_FORMAT, CodePattern.IF_NOT_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.6364,
        CodePattern.INIT_DEFAULT_VALUE: 0.3636,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.GENERATOR_EXPRESSION: 0.5000,
        CodePattern.INIT_EMPTY_LIST: 0.5000,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.GENERATOR_EXPRESSION: 0.4167,
        CodePattern.STRING_FORMAT: 0.3333,
        CodePattern.IF_EMPTY_CHECK: 0.2500,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.IF_TYPE_CHECK): {
        CodePattern.IF_TYPE_CHECK: 0.5714,
        CodePattern.IF_EMPTY_CHECK: 0.2143,
        CodePattern.FUNCTION_TRANSFORMER: 0.2143,
    },
    (CodePattern.UNPACKING, CodePattern.IF_TYPE_CHECK): {
        CodePattern.UNPACKING: 0.4667,
        CodePattern.IF_TYPE_CHECK: 0.3333,
        CodePattern.RETURN_COMPUTED: 0.2000,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.3889,
        CodePattern.TERNARY_EXPRESSION: 0.2222,
        CodePattern.IF_TYPE_CHECK: 0.2222,
        CodePattern.FUNCTION_TRANSFORMER: 0.1667,
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.IF_NOT_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4000,
        CodePattern.IF_NOT_NONE: 0.2667,
        CodePattern.IF_NONE_CHECK: 0.1333,
        CodePattern.RETURN_COMPUTED: 0.1000,
        CodePattern.IF_EMPTY_CHECK: 0.1000,
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 0.6000,
        CodePattern.UNPACKING: 0.4000,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 0.8537,
        CodePattern.TRY_EXCEPT_RERAISE: 0.1463,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.IF_NONE_CHECK): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 0.6250,
        CodePattern.FUNCTION_TRANSFORMER: 0.3750,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.IF_NOT_NONE): {
        CodePattern.IF_NOT_NONE: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.RETURN_LIST): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.7273,
        CodePattern.RETURN_NONE: 0.2727,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.GUARD_CLAUSE: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.INIT_COUNTER, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5000,
        CodePattern.RETURN_NONE: 0.5000,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.IF_TYPE_CHECK): {
        CodePattern.UNPACKING: 0.5714,
        CodePattern.RETURN_COMPUTED: 0.4286,
    },
    (CodePattern.INIT_METHOD, CodePattern.IF_NONE_CHECK): {
        CodePattern.IF_NONE_CHECK: 0.2973,
        CodePattern.RETURN_COMPUTED: 0.2432,
        CodePattern.FUNCTION_TRANSFORMER: 0.1892,
        CodePattern.UNPACKING: 0.1081,
        CodePattern.INIT_EMPTY_LIST: 0.0811,
        CodePattern.INIT_EMPTY_DICT: 0.0811,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5217,
        CodePattern.FUNCTION_TRANSFORMER: 0.2609,
        CodePattern.IF_EMPTY_CHECK: 0.2174,
    },
    (CodePattern.LOOP_FILTER, CodePattern.LOOP_FILTER): {
        CodePattern.LOOP_FILTER: 0.3158,
        CodePattern.IF_TYPE_CHECK: 0.2632,
        CodePattern.RETURN_COMPUTED: 0.2105,
        CodePattern.STRING_FORMAT: 0.2105,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.UNPACKING: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_TRANSFORM: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.4375,
        CodePattern.IF_NOT_NONE: 0.1875,
        CodePattern.FUNCTION_TRANSFORMER: 0.1875,
        CodePattern.INIT_DEFAULT_VALUE: 0.1875,
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.LOOP_FILTER, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4600,
        CodePattern.IF_EMPTY_CHECK: 0.2800,
        CodePattern.RETURN_COMPUTED: 0.1600,
        CodePattern.IF_TYPE_CHECK: 0.1000,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.IF_TYPE_CHECK: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.TRY_EXCEPT_RERAISE: 0.4286,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 0.7083,
        CodePattern.IF_NOT_NONE: 0.1667,
        CodePattern.IF_TYPE_CHECK: 0.1250,
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_NONE: 0.5217,
        CodePattern.RETURN_LIST: 0.1739,
        CodePattern.RETURN_COMPUTED: 0.1739,
        CodePattern.GUARD_CLAUSE: 0.1304,
    },
    (CodePattern.RETURN_LIST, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.5789,
        CodePattern.RETURN_COMPUTED: 0.2105,
        CodePattern.IF_EMPTY_CHECK: 0.2105,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_NOT_NONE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_COMPUTED: 0.4167,
        CodePattern.LOOP_ACCUMULATE: 0.3333,
        CodePattern.FUNCTION_TRANSFORMER: 0.2500,
    },
    (CodePattern.LOOP_FILTER, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.IF_EMPTY_CHECK: 0.3333,
        CodePattern.RETURN_COMPUTED: 0.2500,
        CodePattern.LOGGING_CALL: 0.2222,
        CodePattern.GENERATOR_EXPRESSION: 0.1111,
        CodePattern.UNPACKING: 0.0833,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.IF_NONE_CHECK): {
        CodePattern.INIT_EMPTY_LIST: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LOOP_FILTER): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.UNPACKING): {
        CodePattern.STRING_FORMAT: 0.5000,
        CodePattern.UNPACKING: 0.5000,
    },
    (CodePattern.INIT_COUNTER, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.RETURN_LIST, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_LIST: 0.7273,
        CodePattern.LIST_COMPREHENSION: 0.2727,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.DICT_COMPREHENSION): {
        CodePattern.IF_TYPE_CHECK: 1.0000
    },
    (CodePattern.DICT_COMPREHENSION, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_COMPUTED: 0.4615,
        CodePattern.LOOP_ACCUMULATE: 0.3077,
        CodePattern.IF_NOT_NONE: 0.2308,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.STRING_FORMAT): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.6667,
        CodePattern.RETURN_NONE: 0.3333,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_NONE_CHECK): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_COMPUTED: 0.5385,
        CodePattern.LOGGING_CALL: 0.2308,
        CodePattern.GENERATOR_EXPRESSION: 0.2308,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.INIT_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.IF_TYPE_CHECK: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 0.4167,
        CodePattern.LOGGING_CALL: 0.3333,
        CodePattern.RETURN_COMPUTED: 0.2500,
    },
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.TRY_EXCEPT_PASS: 0.4286,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.5625,
        CodePattern.RETURN_NONE: 0.2500,
        CodePattern.TERNARY_EXPRESSION: 0.1875,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.GUARD_CLAUSE: 0.4286,
    },
    (CodePattern.LOOP_FILTER, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_COMPUTED: 0.7273,
        CodePattern.LOGGING_CALL: 0.2727,
    },
    (CodePattern.UNPACKING, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 0.3182,
        CodePattern.STRING_FORMAT: 0.2273,
        CodePattern.UNPACKING: 0.1818,
        CodePattern.FUNCTION_TRANSFORMER: 0.1364,
        CodePattern.LOOP_ACCUMULATE: 0.1364,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_COUNTER: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.UNPACKING): {
        CodePattern.RETURN_COMPUTED: 0.4000,
        CodePattern.IF_EMPTY_CHECK: 0.3000,
        CodePattern.UNPACKING: 0.3000,
    },
    (CodePattern.RETURN_NONE, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.LOOP_FILTER): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_FILTER): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.LIST_COMPREHENSION): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.RETURN_BOOL): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.LOOP_FILTER): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.6364,
        CodePattern.LOOP_TRANSFORM: 0.3636,
    },
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.6250,
        CodePattern.RETURN_NONE: 0.3750,
    },
    (CodePattern.LOOP_FILTER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.IF_EMPTY_CHECK: 1.0000
    },
    (CodePattern.LOOP_FILTER, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.6667,
        CodePattern.IF_EMPTY_CHECK: 0.3333,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.DICT_COMPREHENSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_COMPUTED: 0.3871,
        CodePattern.IF_EMPTY_CHECK: 0.1935,
        CodePattern.LOGGING_CALL: 0.1613,
        CodePattern.STRING_FORMAT: 0.1613,
        CodePattern.RETURN_NONE: 0.0968,
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_DICT_ITEMS: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.7059,
        CodePattern.RETURN_NONE: 0.2941,
    },
    (CodePattern.RETURN_NONE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.RETURN_COMPUTED: 0.5161,
        CodePattern.GUARD_CLAUSE: 0.1935,
        CodePattern.IF_TYPE_CHECK: 0.0968,
        CodePattern.TERNARY_EXPRESSION: 0.0968,
        CodePattern.TRY_EXCEPT_PASS: 0.0968,
    },
    (CodePattern.RETURN_BOOL, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.LOGGING_CALL): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4500,
        CodePattern.GUARD_CLAUSE: 0.2500,
        CodePattern.FUNCTION_TRANSFORMER: 0.1500,
        CodePattern.IF_NONE_CHECK: 0.1500,
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.4167,
        CodePattern.RETURN_BOOL: 0.3333,
        CodePattern.RETURN_NONE: 0.2500,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_BOOL): {
        CodePattern.RETURN_COMPUTED: 0.3810,
        CodePattern.GUARD_CLAUSE: 0.2857,
        CodePattern.RETURN_BOOL: 0.1905,
        CodePattern.IF_EMPTY_CHECK: 0.1429,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_BOOL): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_DICT): {
        CodePattern.DICT_COMPREHENSION: 1.0000
    },
    (CodePattern.RETURN_DICT, CodePattern.DICT_COMPREHENSION): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_COUNTER, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOOP_DICT_ITEMS, CodePattern.RETURN_LIST): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.TRY_EXCEPT_LOG): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.TRY_EXCEPT_LOG, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 0.7500,
        CodePattern.RETURN_COMPUTED: 0.2500,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.TRY_EXCEPT_LOG): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.5833,
        CodePattern.RETURN_NONE: 0.1389,
        CodePattern.RETURN_BOOL: 0.1389,
        CodePattern.RETURN_LIST: 0.1389,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_BOOL): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 0.5556,
        CodePattern.RETURN_COMPUTED: 0.4444,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_LIST): {
        CodePattern.IF_TYPE_CHECK: 0.3333,
        CodePattern.FUNCTION_TRANSFORMER: 0.2667,
        CodePattern.RETURN_COMPUTED: 0.2000,
        CodePattern.LOGGING_CALL: 0.2000,
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.UNPACKING): {
        CodePattern.IF_EMPTY_CHECK: 1.0000
    },
    (CodePattern.LOOP_FILTER, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.STRING_FORMAT: 0.5714,
        CodePattern.LOOP_ACCUMULATE: 0.4286,
    },
    (CodePattern.UNPACKING, CodePattern.RETURN_DICT): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_NONE: 1.0000
    },
    (CodePattern.INIT_EMPTY_DICT, CodePattern.TRY_EXCEPT_PASS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.INIT_EMPTY_LIST: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.PROPERTY_GETTER): {
        CodePattern.UNPACKING: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.IF_EMPTY_CHECK: 0.5000,
        CodePattern.GUARD_CLAUSE: 0.5000,
    },
    (CodePattern.LOGGING_CALL, CodePattern.IF_TYPE_CHECK): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.LOOP_ZIP, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.PROPERTY_GETTER): {
        CodePattern.LIST_COMPREHENSION: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.LIST_COMPREHENSION): {
        CodePattern.PROPERTY_GETTER: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_COUNTER): {
        CodePattern.IF_EMPTY_CHECK: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.CLASS_METHOD, CodePattern.INIT_EMPTY_DICT): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.LIST_COMPREHENSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.UNPACKING): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOOP_ZIP): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_BOOL, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.RETURN_LIST): {
        CodePattern.LOGGING_CALL: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.STRING_FORMAT): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
}


def get_next_pattern_probabilities(pattern_sequence):
    """
    Get probability distribution for next semantic pattern.

    Args:
        pattern_sequence: Tuple of CodePattern enums representing current context

    Returns:
        Dictionary mapping CodePattern to probabilities, or None if state unknown
    """
    return probabilities.get(pattern_sequence)


def get_top_k_patterns(pattern_sequence, k=5):
    """
    Get top-k most likely next patterns.

    Args:
        pattern_sequence: Tuple of CodePattern enums representing current context
        k: Number of top predictions to return

    Returns:
        List of (CodePattern, probability) tuples, sorted by probability descending
    """
    probs = get_next_pattern_probabilities(pattern_sequence)
    if probs is None:
        return []

    return sorted(probs.items(), key=lambda x: x[1], reverse=True)[:k]


def suggest_next_patterns(current_patterns, k=5):
    """
    Convenience function: given recent patterns, suggest what comes next.

    Args:
        current_patterns: List of recent CodePattern enums
        k: Number of suggestions

    Returns:
        List of (CodePattern, probability) tuples
    """
    if not current_patterns:
        return []

    # Try with full context
    if len(current_patterns) >= MARKOV_ORDER:
        context = tuple(current_patterns[-MARKOV_ORDER:])
    else:
        context = tuple(current_patterns)

    suggestions = get_top_k_patterns(context, k)

    # If no suggestions, try with shorter context
    if not suggestions and len(current_patterns) > 1:
        context = (current_patterns[-1],)
        suggestions = get_top_k_patterns(context, k)

    return suggestions


# Model metadata
MARKOV_ORDER = 2
FILES_PROCESSED = 0
UNIQUE_SEQUENCES = 635
MIN_COUNT_THRESHOLD = 3
TOTAL_PATTERNS_TRAINED = 55315
