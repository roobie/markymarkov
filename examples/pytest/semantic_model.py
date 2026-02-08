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
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 194,
            CodePattern.INIT_DEFAULT_VALUE: 24,
            CodePattern.RETURN_COMPUTED: 20,
            CodePattern.CONTEXT_MANAGER: 18,
            CodePattern.INIT_METHOD: 11,
            CodePattern.FUNCTION_VALIDATOR: 11,
            CodePattern.PROPERTY_GETTER: 9,
            CodePattern.TERNARY_EXPRESSION: 8,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.UNPACKING: 4,
            CodePattern.CLASS_METHOD: 4,
            CodePattern.LIST_COMPREHENSION: 3,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.TRY_FINALLY: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 178,
            CodePattern.GUARD_CLAUSE: 45,
            CodePattern.IF_EMPTY_CHECK: 23,
            CodePattern.LIST_COMPREHENSION: 19,
            CodePattern.FUNCTION_TRANSFORMER: 18,
            CodePattern.INIT_DEFAULT_VALUE: 13,
            CodePattern.IF_NONE_CHECK: 12,
            CodePattern.INIT_EMPTY_LIST: 10,
            CodePattern.IF_TYPE_CHECK: 9,
            CodePattern.IF_NOT_NONE: 9,
            CodePattern.TRY_EXCEPT_RERAISE: 8,
            CodePattern.TERNARY_EXPRESSION: 7,
            CodePattern.UNPACKING: 7,
            CodePattern.DICT_GET_DEFAULT: 7,
            CodePattern.LOOP_FILTER: 6,
            CodePattern.CONTEXT_MANAGER: 6,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.EARLY_RETURN_SUCCESS: 5,
            CodePattern.LOOP_ACCUMULATE: 5,
            CodePattern.RETURN_NONE: 4,
            CodePattern.RETURN_BOOL: 4,
            CodePattern.TRY_FINALLY: 4,
            CodePattern.INIT_COUNTER: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.LOGGING_CALL: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.CONTEXT_MANAGER: 4}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.STRING_FORMAT: 7,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.STRING_FORMAT: 164,
            CodePattern.CONTEXT_MANAGER: 17,
            CodePattern.INIT_DEFAULT_VALUE: 11,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.TRY_FINALLY: 7,
            CodePattern.RETURN_COMPUTED: 7,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.LOGGING_CALL: 6,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.STRING_FORMAT: 4,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 36,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.GUARD_CLAUSE: 7,
            CodePattern.RETURN_BOOL: 4,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.DICT_GET_DEFAULT): Counter(
        {CodePattern.RETURN_COMPUTED: 5, CodePattern.UNPACKING: 3}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 104,
            CodePattern.FUNCTION_TRANSFORMER: 10,
            CodePattern.CONTEXT_MANAGER: 8,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.LIST_COMPREHENSION: 7,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.GENERATOR_EXPRESSION: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 8,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.UNPACKING: 6,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 14,
            CodePattern.FUNCTION_TRANSFORMER: 12,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 7}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 14,
            CodePattern.PROPERTY_GETTER: 5,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.IF_NOT_NONE: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.IF_NONE_CHECK: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.CONTEXT_MANAGER: 11,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 15,
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 27,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.UNPACKING: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.INIT_METHOD: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.TERNARY_EXPRESSION: 4,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.UNPACKING: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NONE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.RETURN_BOOL: 4,
            CodePattern.RETURN_NONE: 4,
        }
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6, CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.RETURN_NONE, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.PROPERTY_GETTER: 29,
            CodePattern.FUNCTION_TRANSFORMER: 14,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.INIT_METHOD: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.INIT_METHOD, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 7}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 8}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 31, CodePattern.PROPERTY_GETTER: 13}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.PROPERTY_GETTER): Counter(
        {
            CodePattern.PROPERTY_GETTER: 13,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.RETURN_COMPUTED: 5,
        }
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 5, CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 13,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 269,
            CodePattern.INIT_DEFAULT_VALUE: 23,
            CodePattern.LOGGING_CALL: 21,
            CodePattern.UNPACKING: 20,
            CodePattern.FUNCTION_TRANSFORMER: 18,
            CodePattern.STRING_FORMAT: 6,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.INIT_EMPTY_LIST: 3,
            CodePattern.INIT_METHOD: 3,
            CodePattern.TRY_FINALLY: 3,
        }
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.UNPACKING): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 17,
            CodePattern.UNPACKING: 10,
            CodePattern.LIST_COMPREHENSION: 4,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 6, CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.TERNARY_EXPRESSION: 3, CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.TERNARY_EXPRESSION): Counter(
        {
            CodePattern.TERNARY_EXPRESSION: 10,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 12,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.UNPACKING: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 8,
            CodePattern.INIT_DEFAULT_VALUE: 6,
            CodePattern.TERNARY_EXPRESSION: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 4}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.UNPACKING: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.LOOP_FILTER: 3,
            CodePattern.INIT_EMPTY_LIST: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_METHOD): Counter(
        {
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.PROPERTY_GETTER: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.UNPACKING): Counter(
        {
            CodePattern.UNPACKING: 5,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 111,
            CodePattern.FUNCTION_TRANSFORMER: 22,
            CodePattern.CONTEXT_MANAGER: 10,
            CodePattern.INIT_COUNTER: 8,
            CodePattern.UNPACKING: 7,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.LOOP_ACCUMULATE: 6,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.INIT_METHOD: 5,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.FUNCTION_VALIDATOR: 3,
        }
    ),
    (CodePattern.UNPACKING, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 3}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_FILTER): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.IF_TYPE_CHECK: 3,
        }
    ),
    (CodePattern.LOOP_FILTER, CodePattern.UNPACKING): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 7, CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LOOP_ACCUMULATE): Counter(
        {
            CodePattern.LOOP_ACCUMULATE: 34,
            CodePattern.RETURN_COMPUTED: 12,
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.LIST_COMPREHENSION: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.LOOP_ENUMERATE: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 4}
    ),
    (CodePattern.UNPACKING, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.UNPACKING: 14, CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LIST_COMPREHENSION): Counter(
        {
            CodePattern.LIST_COMPREHENSION: 8,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.CONTEXT_MANAGER: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 6, CodePattern.UNPACKING: 3}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 10, CodePattern.INIT_COUNTER: 3}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 7, CodePattern.INIT_COUNTER: 5}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 4}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 20,
            CodePattern.RETURN_COMPUTED: 10,
            CodePattern.INIT_METHOD: 4,
            CodePattern.GUARD_CLAUSE: 4,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 37,
            CodePattern.RETURN_COMPUTED: 13,
            CodePattern.STRING_FORMAT: 7,
            CodePattern.FUNCTION_VALIDATOR: 7,
            CodePattern.IF_TYPE_CHECK: 5,
            CodePattern.INIT_METHOD: 5,
            CodePattern.CONTEXT_MANAGER: 4,
            CodePattern.GENERATOR_EXPRESSION: 3,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.STATIC_METHOD: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_NONE): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 10,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.GUARD_CLAUSE: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.INIT_EMPTY_LIST: 3,
        }
    ),
    (CodePattern.DICT_COMPREHENSION, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.LOOP_ACCUMULATE: 5}
    ),
    (CodePattern.INIT_COUNTER, CodePattern.INIT_COUNTER): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 9, CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.RETURN_BOOL: 8,
            CodePattern.GUARD_CLAUSE: 7,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.INIT_DEFAULT_VALUE: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.TRY_FINALLY, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.TRY_FINALLY: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.STRING_FORMAT: 16, CodePattern.CONTEXT_MANAGER: 7}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 13,
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.UNPACKING: 5,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 4}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_EMPTY_LIST): Counter(
        {
            CodePattern.LOOP_FILTER: 9,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.LOOP_TRANSFORM: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.TERNARY_EXPRESSION): Counter(
        {CodePattern.TERNARY_EXPRESSION: 5}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 6, CodePattern.TRY_EXCEPT_RERAISE: 3}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 11, CodePattern.UNPACKING: 11}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 24,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.UNPACKING: 3,
            CodePattern.FUNCTION_TRANSFORMER: 3,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.TRY_FINALLY, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.STATIC_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 4, CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {
            CodePattern.STRING_FORMAT: 5,
            CodePattern.INIT_DEFAULT_VALUE: 4,
            CodePattern.IF_EMPTY_CHECK: 4,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.UNPACKING): Counter(
        {CodePattern.LIST_COMPREHENSION: 10, CodePattern.UNPACKING: 4}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.LOGGING_CALL): Counter(
        {
            CodePattern.LOGGING_CALL: 23,
            CodePattern.CONTEXT_MANAGER: 14,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.STRING_FORMAT: 3,
        }
    ),
    (CodePattern.LOGGING_CALL, CodePattern.CONTEXT_MANAGER): Counter(
        {CodePattern.CONTEXT_MANAGER: 23, CodePattern.LOGGING_CALL: 16}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.CONTEXT_MANAGER: 20, CodePattern.LOGGING_CALL: 17}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.CONTEXT_MANAGER: 3}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.LIST_COMPREHENSION: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 7, CodePattern.PROPERTY_GETTER: 4}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.CLASS_METHOD: 3}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 8}
    ),
    (CodePattern.INIT_METHOD, CodePattern.INIT_METHOD): Counter(
        {CodePattern.INIT_METHOD: 10}
    ),
    (CodePattern.STATIC_METHOD, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.RETURN_NONE: 22,
            CodePattern.RETURN_COMPUTED: 19,
            CodePattern.RETURN_LIST: 5,
            CodePattern.STRING_FORMAT: 3,
            CodePattern.UNPACKING: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 43,
            CodePattern.RETURN_NONE: 35,
            CodePattern.RETURN_BOOL: 8,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.LOGGING_CALL: 4,
            CodePattern.TERNARY_EXPRESSION: 4,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.GUARD_CLAUSE: 10,
            CodePattern.RETURN_COMPUTED: 7,
            CodePattern.RETURN_NONE: 4,
        }
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_FILTER: 7, CodePattern.INIT_EMPTY_LIST: 4}
    ),
    (CodePattern.CLASS_METHOD, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.STRING_FORMAT: 4}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.LIST_COMPREHENSION: 3}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 10, CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.UNPACKING): Counter(
        {CodePattern.UNPACKING: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 7}
    ),
    (CodePattern.CLASS_METHOD, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.CLASS_METHOD: 5,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.PROPERTY_GETTER: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.GENERATOR_EXPRESSION): Counter(
        {
            CodePattern.STRING_FORMAT: 6,
            CodePattern.FUNCTION_TRANSFORMER: 4,
            CodePattern.PROPERTY_GETTER: 4,
            CodePattern.RETURN_COMPUTED: 4,
        }
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 10,
            CodePattern.STRING_FORMAT: 5,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.RETURN_COMPUTED: 3,
            CodePattern.INIT_METHOD: 3,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.RETURN_COMPUTED: 5, CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 9, CodePattern.IF_TYPE_CHECK: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 6, CodePattern.IF_NONE_CHECK: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.STRING_FORMAT): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 16,
            CodePattern.GENERATOR_EXPRESSION: 9,
            CodePattern.STRING_FORMAT: 8,
            CodePattern.RETURN_COMPUTED: 4,
        }
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.CONTEXT_MANAGER): Counter(
        {
            CodePattern.CONTEXT_MANAGER: 7,
            CodePattern.FUNCTION_TRANSFORMER: 7,
            CodePattern.RETURN_COMPUTED: 6,
        }
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_NONE): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 11,
            CodePattern.GUARD_CLAUSE: 10,
            CodePattern.IF_NOT_NONE: 8,
            CodePattern.IF_EMPTY_CHECK: 7,
            CodePattern.INIT_DEFAULT_VALUE: 5,
            CodePattern.TERNARY_EXPRESSION: 5,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.DICT_GET_DEFAULT: 3,
        }
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.STRING_FORMAT: 6, CodePattern.LOGGING_CALL: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.GENERATOR_EXPRESSION: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.LIST_COMPREHENSION): Counter(
        {CodePattern.LIST_COMPREHENSION: 4, CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 8}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.GUARD_CLAUSE: 27,
            CodePattern.RETURN_COMPUTED: 21,
            CodePattern.RETURN_NONE: 16,
            CodePattern.FUNCTION_TRANSFORMER: 13,
            CodePattern.RETURN_BOOL: 5,
            CodePattern.STRING_FORMAT: 4,
            CodePattern.INIT_METHOD: 3,
            CodePattern.LOOP_ACCUMULATE: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_NONE): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 24}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 9}
    ),
    (CodePattern.CONTEXT_MANAGER, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.STRING_FORMAT: 18, CodePattern.CONTEXT_MANAGER: 7}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.INIT_DEFAULT_VALUE: 7,
            CodePattern.RETURN_COMPUTED: 4,
            CodePattern.FUNCTION_TRANSFORMER: 3,
        }
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_EMPTY_CHECK): Counter(
        {
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.LOOP_ACCUMULATE: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_VALIDATOR): Counter(
        {
            CodePattern.GUARD_CLAUSE: 12,
            CodePattern.IF_NONE_CHECK: 6,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.IF_EMPTY_CHECK: 3,
        }
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.RETURN_BOOL: 5}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_COMPUTED: 30,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.RETURN_BOOL: 3,
        }
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 6,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.RETURN_NONE: 3,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.CLASS_METHOD: 3,
        }
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 6, CodePattern.IF_EMPTY_CHECK: 4}
    ),
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_TRANSFORM): Counter(
        {
            CodePattern.STRING_FORMAT: 6,
            CodePattern.LOOP_ENUMERATE: 3,
            CodePattern.RETURN_COMPUTED: 3,
        }
    ),
    (CodePattern.STRING_FORMAT, CodePattern.INIT_EMPTY_LIST): Counter(
        {CodePattern.LOOP_TRANSFORM: 7}
    ),
    (CodePattern.LOOP_TRANSFORM, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.INIT_EMPTY_LIST: 5}
    ),
    (CodePattern.STRING_FORMAT, CodePattern.TRY_FINALLY): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_METHOD): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 4}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.LOGGING_CALL, CodePattern.STRING_FORMAT): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 4, CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.LIST_COMPREHENSION: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 9}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_TYPE_CHECK): Counter(
        {
            CodePattern.RETURN_COMPUTED: 15,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_COMPUTED): Counter(
        {
            CodePattern.FUNCTION_TRANSFORMER: 13,
            CodePattern.RETURN_NONE: 6,
            CodePattern.RETURN_COMPUTED: 5,
            CodePattern.IF_TYPE_CHECK: 4,
            CodePattern.GUARD_CLAUSE: 3,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {
            CodePattern.GUARD_CLAUSE: 11,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.FUNCTION_TRANSFORMER: 5,
            CodePattern.IF_EMPTY_CHECK: 5,
            CodePattern.DICT_GET_DEFAULT: 4,
            CodePattern.IF_NOT_NONE: 3,
            CodePattern.IF_TYPE_CHECK: 3,
            CodePattern.RETURN_NONE: 3,
        }
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 18, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.LOOP_ACCUMULATE, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.TERNARY_EXPRESSION: 3, CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.LOOP_ENUMERATE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 11, CodePattern.IF_NONE_CHECK: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_BOOL: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_FILTER): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NONE_CHECK): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.INIT_DEFAULT_VALUE): Counter(
        {CodePattern.INIT_METHOD: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_ENUMERATE): Counter(
        {CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.PROPERTY_GETTER): Counter(
        {CodePattern.RETURN_COMPUTED: 4}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOGGING_CALL): Counter(
        {CodePattern.STRING_FORMAT: 3}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.GUARD_CLAUSE): Counter(
        {
            CodePattern.RETURN_NONE: 8,
            CodePattern.RETURN_BOOL: 7,
            CodePattern.GUARD_CLAUSE: 6,
            CodePattern.RETURN_COMPUTED: 4,
        }
    ),
    (CodePattern.RETURN_NONE, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_NONE: 8}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.IF_TYPE_CHECK: 3}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 9}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_BOOL): Counter(
        {
            CodePattern.GUARD_CLAUSE: 3,
            CodePattern.IF_EMPTY_CHECK: 3,
            CodePattern.RETURN_BOOL: 3,
        }
    ),
    (CodePattern.RETURN_BOOL, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_BOOL: 28}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_BOOL): Counter(
        {
            CodePattern.GUARD_CLAUSE: 23,
            CodePattern.RETURN_BOOL: 12,
            CodePattern.RETURN_COMPUTED: 6,
            CodePattern.IF_EMPTY_CHECK: 4,
            CodePattern.FUNCTION_TRANSFORMER: 4,
        }
    ),
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_BOOL: 6}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.RETURN_BOOL: 5, CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6}
    ),
    (CodePattern.LOOP_FILTER, CodePattern.IF_TYPE_CHECK): Counter(
        {CodePattern.RETURN_COMPUTED: 3, CodePattern.IF_TYPE_CHECK: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.RETURN_NONE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_NONE: 14}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 4}
    ),
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 4}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_EXCEPT_RERAISE): Counter(
        {CodePattern.RETURN_COMPUTED: 8, CodePattern.IF_EMPTY_CHECK: 3}
    ),
    (CodePattern.RETURN_NONE, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.IF_NOT_NONE: 6}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.FUNCTION_TRANSFORMER): Counter(
        {CodePattern.GUARD_CLAUSE: 3, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 5}
    ),
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.RETURN_COMPUTED: 6}
    ),
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.RETURN_NONE: 5, CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 6, CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_NOT_NONE, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_NONE: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_BOOL): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.GENERATOR_EXPRESSION): Counter(
        {CodePattern.RETURN_BOOL: 3}
    ),
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.IF_EMPTY_CHECK: 4}
    ),
    (CodePattern.UNPACKING, CodePattern.IF_EMPTY_CHECK): Counter(
        {CodePattern.INIT_DEFAULT_VALUE: 3}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.UNPACKING): Counter(
        {CodePattern.IF_EMPTY_CHECK: 4}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.PROPERTY_GETTER, CodePattern.RETURN_NONE): Counter(
        {CodePattern.PROPERTY_GETTER: 4}
    ),
    (CodePattern.RETURN_LIST, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_LIST: 3}
    ),
    (CodePattern.RETURN_LIST, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.RETURN_COMPUTED): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 5}
    ),
    (CodePattern.IF_TYPE_CHECK, CodePattern.GUARD_CLAUSE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.IF_NONE_CHECK, CodePattern.CLASS_METHOD): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_VALIDATOR): Counter(
        {CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.UNPACKING, CodePattern.LOOP_ACCUMULATE): Counter(
        {CodePattern.LOOP_ACCUMULATE: 3}
    ),
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_LIST): Counter(
        {CodePattern.GUARD_CLAUSE: 3}
    ),
    (CodePattern.TRY_FINALLY, CodePattern.IF_NOT_NONE): Counter(
        {CodePattern.FUNCTION_TRANSFORMER: 3}
    ),
    (CodePattern.RETURN_COMPUTED, CodePattern.EARLY_RETURN_SUCCESS): Counter(
        {CodePattern.RETURN_COMPUTED: 3}
    ),
}

# Pattern transition probabilities
probabilities = {
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.5969,
        CodePattern.INIT_DEFAULT_VALUE: 0.0738,
        CodePattern.RETURN_COMPUTED: 0.0615,
        CodePattern.CONTEXT_MANAGER: 0.0554,
        CodePattern.INIT_METHOD: 0.0338,
        CodePattern.FUNCTION_VALIDATOR: 0.0338,
        CodePattern.PROPERTY_GETTER: 0.0277,
        CodePattern.TERNARY_EXPRESSION: 0.0246,
        CodePattern.STRING_FORMAT: 0.0246,
        CodePattern.IF_EMPTY_CHECK: 0.0154,
        CodePattern.UNPACKING: 0.0123,
        CodePattern.CLASS_METHOD: 0.0123,
        CodePattern.LIST_COMPREHENSION: 0.0092,
        CodePattern.GENERATOR_EXPRESSION: 0.0092,
        CodePattern.TRY_FINALLY: 0.0092,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4300,
        CodePattern.GUARD_CLAUSE: 0.1087,
        CodePattern.IF_EMPTY_CHECK: 0.0556,
        CodePattern.LIST_COMPREHENSION: 0.0459,
        CodePattern.FUNCTION_TRANSFORMER: 0.0435,
        CodePattern.INIT_DEFAULT_VALUE: 0.0314,
        CodePattern.IF_NONE_CHECK: 0.0290,
        CodePattern.INIT_EMPTY_LIST: 0.0242,
        CodePattern.IF_TYPE_CHECK: 0.0217,
        CodePattern.IF_NOT_NONE: 0.0217,
        CodePattern.TRY_EXCEPT_RERAISE: 0.0193,
        CodePattern.TERNARY_EXPRESSION: 0.0169,
        CodePattern.UNPACKING: 0.0169,
        CodePattern.DICT_GET_DEFAULT: 0.0169,
        CodePattern.LOOP_FILTER: 0.0145,
        CodePattern.CONTEXT_MANAGER: 0.0145,
        CodePattern.STRING_FORMAT: 0.0121,
        CodePattern.EARLY_RETURN_SUCCESS: 0.0121,
        CodePattern.LOOP_ACCUMULATE: 0.0121,
        CodePattern.RETURN_NONE: 0.0097,
        CodePattern.RETURN_BOOL: 0.0097,
        CodePattern.TRY_FINALLY: 0.0097,
        CodePattern.INIT_COUNTER: 0.0097,
        CodePattern.INIT_METHOD: 0.0072,
        CodePattern.LOGGING_CALL: 0.0072,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LIST_COMPREHENSION): {
        CodePattern.RETURN_COMPUTED: 0.4375,
        CodePattern.FUNCTION_TRANSFORMER: 0.3750,
        CodePattern.STRING_FORMAT: 0.1875,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 0.3182,
        CodePattern.INIT_DEFAULT_VALUE: 0.3182,
        CodePattern.FUNCTION_TRANSFORMER: 0.2273,
        CodePattern.CONTEXT_MANAGER: 0.1364,
    },
    (CodePattern.STRING_FORMAT, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 0.7700,
        CodePattern.CONTEXT_MANAGER: 0.0798,
        CodePattern.INIT_DEFAULT_VALUE: 0.0516,
        CodePattern.FUNCTION_TRANSFORMER: 0.0329,
        CodePattern.TRY_FINALLY: 0.0329,
        CodePattern.RETURN_COMPUTED: 0.0329,
    },
    (CodePattern.STRING_FORMAT, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.LOGGING_CALL: 0.3158,
        CodePattern.INIT_DEFAULT_VALUE: 0.2632,
        CodePattern.CONTEXT_MANAGER: 0.2105,
        CodePattern.STRING_FORMAT: 0.2105,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.6000,
        CodePattern.FUNCTION_TRANSFORMER: 0.1167,
        CodePattern.GUARD_CLAUSE: 0.1167,
        CodePattern.RETURN_BOOL: 0.0667,
        CodePattern.IF_TYPE_CHECK: 0.0500,
        CodePattern.INIT_DEFAULT_VALUE: 0.0500,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.DICT_GET_DEFAULT): {
        CodePattern.RETURN_COMPUTED: 0.6250,
        CodePattern.UNPACKING: 0.3750,
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.7222,
        CodePattern.FUNCTION_TRANSFORMER: 0.0694,
        CodePattern.CONTEXT_MANAGER: 0.0556,
        CodePattern.INIT_DEFAULT_VALUE: 0.0486,
        CodePattern.LIST_COMPREHENSION: 0.0486,
        CodePattern.TERNARY_EXPRESSION: 0.0347,
        CodePattern.GENERATOR_EXPRESSION: 0.0208,
    },
    (CodePattern.UNPACKING, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.4000,
        CodePattern.FUNCTION_TRANSFORMER: 0.3000,
        CodePattern.UNPACKING: 0.3000,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4242,
        CodePattern.FUNCTION_TRANSFORMER: 0.3636,
        CodePattern.CONTEXT_MANAGER: 0.1212,
        CodePattern.RETURN_COMPUTED: 0.0909,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.INIT_METHOD): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3590,
        CodePattern.PROPERTY_GETTER: 0.1282,
        CodePattern.RETURN_COMPUTED: 0.1026,
        CodePattern.IF_NOT_NONE: 0.1026,
        CodePattern.INIT_METHOD: 0.0769,
        CodePattern.INIT_DEFAULT_VALUE: 0.0769,
        CodePattern.IF_NONE_CHECK: 0.0769,
        CodePattern.IF_EMPTY_CHECK: 0.0769,
    },
    (CodePattern.INIT_METHOD, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3714,
        CodePattern.CONTEXT_MANAGER: 0.3143,
        CodePattern.FUNCTION_TRANSFORMER: 0.1429,
        CodePattern.INIT_DEFAULT_VALUE: 0.0857,
        CodePattern.GUARD_CLAUSE: 0.0857,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.4839,
        CodePattern.IF_EMPTY_CHECK: 0.2258,
        CodePattern.RETURN_COMPUTED: 0.1935,
        CodePattern.LOOP_ACCUMULATE: 0.0968,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.5510,
        CodePattern.INIT_DEFAULT_VALUE: 0.1224,
        CodePattern.GUARD_CLAUSE: 0.1224,
        CodePattern.UNPACKING: 0.0816,
        CodePattern.FUNCTION_TRANSFORMER: 0.0612,
        CodePattern.INIT_METHOD: 0.0612,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 0.3077,
        CodePattern.RETURN_COMPUTED: 0.2308,
        CodePattern.FUNCTION_TRANSFORMER: 0.2308,
        CodePattern.GUARD_CLAUSE: 0.2308,
    },
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.5217,
        CodePattern.IF_TYPE_CHECK: 0.2174,
        CodePattern.UNPACKING: 0.1304,
        CodePattern.FUNCTION_TRANSFORMER: 0.1304,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.3846,
        CodePattern.RETURN_BOOL: 0.3077,
        CodePattern.RETURN_NONE: 0.3077,
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6000,
        CodePattern.RETURN_COMPUTED: 0.4000,
    },
    (CodePattern.RETURN_NONE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.RETURN_COMPUTED): {
        CodePattern.PROPERTY_GETTER: 0.5273,
        CodePattern.FUNCTION_TRANSFORMER: 0.2545,
        CodePattern.STRING_FORMAT: 0.1091,
        CodePattern.INIT_METHOD: 0.0545,
        CodePattern.RETURN_COMPUTED: 0.0545,
    },
    (CodePattern.INIT_METHOD, CodePattern.RETURN_COMPUTED): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.GUARD_CLAUSE: 0.3750,
        CodePattern.RETURN_COMPUTED: 0.2500,
        CodePattern.INIT_DEFAULT_VALUE: 0.1875,
        CodePattern.FUNCTION_TRANSFORMER: 0.1875,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 0.7045,
        CodePattern.PROPERTY_GETTER: 0.2955,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.PROPERTY_GETTER): {
        CodePattern.PROPERTY_GETTER: 0.5652,
        CodePattern.FUNCTION_TRANSFORMER: 0.2174,
        CodePattern.RETURN_COMPUTED: 0.2174,
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.6250,
        CodePattern.GUARD_CLAUSE: 0.3750,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.6190,
        CodePattern.FUNCTION_TRANSFORMER: 0.2381,
        CodePattern.RETURN_COMPUTED: 0.1429,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.7251,
        CodePattern.INIT_DEFAULT_VALUE: 0.0620,
        CodePattern.LOGGING_CALL: 0.0566,
        CodePattern.UNPACKING: 0.0539,
        CodePattern.FUNCTION_TRANSFORMER: 0.0485,
        CodePattern.STRING_FORMAT: 0.0162,
        CodePattern.LIST_COMPREHENSION: 0.0135,
        CodePattern.INIT_EMPTY_LIST: 0.0081,
        CodePattern.INIT_METHOD: 0.0081,
        CodePattern.TRY_FINALLY: 0.0081,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.UNPACKING): {
        CodePattern.CONTEXT_MANAGER: 0.4359,
        CodePattern.UNPACKING: 0.2564,
        CodePattern.LIST_COMPREHENSION: 0.1026,
        CodePattern.INIT_DEFAULT_VALUE: 0.1026,
        CodePattern.FUNCTION_TRANSFORMER: 0.1026,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.6667,
        CodePattern.INIT_DEFAULT_VALUE: 0.3333,
    },
    (CodePattern.UNPACKING, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 0.5000,
        CodePattern.INIT_DEFAULT_VALUE: 0.5000,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 0.5882,
        CodePattern.FUNCTION_TRANSFORMER: 0.2353,
        CodePattern.CONTEXT_MANAGER: 0.1765,
    },
    (CodePattern.UNPACKING, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5455,
        CodePattern.CONTEXT_MANAGER: 0.1818,
        CodePattern.UNPACKING: 0.1364,
        CodePattern.FUNCTION_TRANSFORMER: 0.1364,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.4706,
        CodePattern.INIT_DEFAULT_VALUE: 0.3529,
        CodePattern.TERNARY_EXPRESSION: 0.1765,
    },
    (CodePattern.UNPACKING, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.3636,
        CodePattern.INIT_DEFAULT_VALUE: 0.1212,
        CodePattern.GUARD_CLAUSE: 0.1212,
        CodePattern.UNPACKING: 0.1212,
        CodePattern.INIT_METHOD: 0.0909,
        CodePattern.LOOP_FILTER: 0.0909,
        CodePattern.INIT_EMPTY_LIST: 0.0909,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_METHOD): {
        CodePattern.RETURN_COMPUTED: 0.4615,
        CodePattern.FUNCTION_TRANSFORMER: 0.3077,
        CodePattern.PROPERTY_GETTER: 0.2308,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.UNPACKING): {
        CodePattern.UNPACKING: 0.3125,
        CodePattern.FUNCTION_TRANSFORMER: 0.3125,
        CodePattern.RETURN_COMPUTED: 0.1875,
        CodePattern.IF_TYPE_CHECK: 0.1875,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5842,
        CodePattern.FUNCTION_TRANSFORMER: 0.1158,
        CodePattern.CONTEXT_MANAGER: 0.0526,
        CodePattern.INIT_COUNTER: 0.0421,
        CodePattern.UNPACKING: 0.0368,
        CodePattern.STRING_FORMAT: 0.0368,
        CodePattern.LOOP_ACCUMULATE: 0.0316,
        CodePattern.RETURN_COMPUTED: 0.0263,
        CodePattern.INIT_METHOD: 0.0263,
        CodePattern.IF_NOT_NONE: 0.0158,
        CodePattern.IF_EMPTY_CHECK: 0.0158,
        CodePattern.FUNCTION_VALIDATOR: 0.0158,
    },
    (CodePattern.UNPACKING, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 1.0000
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_FILTER): {
        CodePattern.IF_EMPTY_CHECK: 0.4667,
        CodePattern.RETURN_COMPUTED: 0.3333,
        CodePattern.IF_TYPE_CHECK: 0.2000,
    },
    (CodePattern.LOOP_FILTER, CodePattern.UNPACKING): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.7000,
        CodePattern.INIT_DEFAULT_VALUE: 0.3000,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 0.5312,
        CodePattern.RETURN_COMPUTED: 0.1875,
        CodePattern.FUNCTION_TRANSFORMER: 0.0938,
        CodePattern.LIST_COMPREHENSION: 0.0781,
        CodePattern.IF_EMPTY_CHECK: 0.0625,
        CodePattern.LOOP_ENUMERATE: 0.0469,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.LIST_COMPREHENSION): {
        CodePattern.UNPACKING: 0.8235,
        CodePattern.CONTEXT_MANAGER: 0.1765,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 0.4444,
        CodePattern.INIT_DEFAULT_VALUE: 0.3889,
        CodePattern.CONTEXT_MANAGER: 0.1667,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.6667,
        CodePattern.UNPACKING: 0.3333,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_DEFAULT_VALUE: 0.7692,
        CodePattern.INIT_COUNTER: 0.2308,
    },
    (CodePattern.INIT_COUNTER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5833,
        CodePattern.INIT_COUNTER: 0.4167,
    },
    (CodePattern.INIT_COUNTER, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.LIST_COMPREHENSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.STRING_FORMAT): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4545,
        CodePattern.RETURN_COMPUTED: 0.2273,
        CodePattern.INIT_METHOD: 0.0909,
        CodePattern.GUARD_CLAUSE: 0.0909,
        CodePattern.STRING_FORMAT: 0.0682,
        CodePattern.UNPACKING: 0.0682,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4253,
        CodePattern.RETURN_COMPUTED: 0.1494,
        CodePattern.STRING_FORMAT: 0.0805,
        CodePattern.FUNCTION_VALIDATOR: 0.0805,
        CodePattern.IF_TYPE_CHECK: 0.0575,
        CodePattern.INIT_METHOD: 0.0575,
        CodePattern.CONTEXT_MANAGER: 0.0460,
        CodePattern.GENERATOR_EXPRESSION: 0.0345,
        CodePattern.INIT_DEFAULT_VALUE: 0.0345,
        CodePattern.STATIC_METHOD: 0.0345,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3704,
        CodePattern.RETURN_COMPUTED: 0.1852,
        CodePattern.GUARD_CLAUSE: 0.1852,
        CodePattern.IF_EMPTY_CHECK: 0.1481,
        CodePattern.INIT_EMPTY_LIST: 0.1111,
    },
    (CodePattern.DICT_COMPREHENSION, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_COUNTER): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.INIT_COUNTER, CodePattern.INIT_COUNTER): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.RETURN_BOOL): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7500,
        CodePattern.CONTEXT_MANAGER: 0.2500,
    },
    (CodePattern.RETURN_BOOL, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_BOOL: 0.2667,
        CodePattern.GUARD_CLAUSE: 0.2333,
        CodePattern.RETURN_COMPUTED: 0.1667,
        CodePattern.IF_EMPTY_CHECK: 0.1333,
        CodePattern.INIT_DEFAULT_VALUE: 0.1000,
        CodePattern.FUNCTION_TRANSFORMER: 0.1000,
    },
    (CodePattern.TRY_FINALLY, CodePattern.TRY_FINALLY): {
        CodePattern.TRY_FINALLY: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.CONTEXT_MANAGER): {
        CodePattern.STRING_FORMAT: 0.6957,
        CodePattern.CONTEXT_MANAGER: 0.3043,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.CONTEXT_MANAGER: 0.4643,
        CodePattern.INIT_DEFAULT_VALUE: 0.2500,
        CodePattern.UNPACKING: 0.1786,
        CodePattern.FUNCTION_TRANSFORMER: 0.1071,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.4091,
        CodePattern.RETURN_COMPUTED: 0.2727,
        CodePattern.LOOP_TRANSFORM: 0.1818,
        CodePattern.FUNCTION_TRANSFORMER: 0.1364,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.TERNARY_EXPRESSION): {
        CodePattern.TERNARY_EXPRESSION: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.6667,
        CodePattern.TRY_EXCEPT_RERAISE: 0.3333,
    },
    (CodePattern.TRY_FINALLY, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.5000,
        CodePattern.UNPACKING: 0.5000,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.6486,
        CodePattern.INIT_DEFAULT_VALUE: 0.1081,
        CodePattern.UNPACKING: 0.0811,
        CodePattern.FUNCTION_TRANSFORMER: 0.0811,
        CodePattern.STRING_FORMAT: 0.0811,
    },
    (CodePattern.TRY_FINALLY, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.STATIC_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5714,
        CodePattern.RETURN_NONE: 0.4286,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.STRING_FORMAT: 0.3846,
        CodePattern.INIT_DEFAULT_VALUE: 0.3077,
        CodePattern.IF_EMPTY_CHECK: 0.3077,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.UNPACKING): {
        CodePattern.LIST_COMPREHENSION: 0.7143,
        CodePattern.UNPACKING: 0.2857,
    },
    (CodePattern.LOGGING_CALL, CodePattern.LOGGING_CALL): {
        CodePattern.LOGGING_CALL: 0.5227,
        CodePattern.CONTEXT_MANAGER: 0.3182,
        CodePattern.FUNCTION_TRANSFORMER: 0.0909,
        CodePattern.STRING_FORMAT: 0.0682,
    },
    (CodePattern.LOGGING_CALL, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.5897,
        CodePattern.LOGGING_CALL: 0.4103,
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.LOGGING_CALL): {
        CodePattern.CONTEXT_MANAGER: 0.5405,
        CodePattern.LOGGING_CALL: 0.4595,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOGGING_CALL): {
        CodePattern.CONTEXT_MANAGER: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 0.6364,
        CodePattern.PROPERTY_GETTER: 0.3636,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.STRING_FORMAT): {
        CodePattern.CLASS_METHOD: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.INIT_METHOD): {
        CodePattern.INIT_METHOD: 1.0000
    },
    (CodePattern.STATIC_METHOD, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_NONE: 0.4231,
        CodePattern.RETURN_COMPUTED: 0.3654,
        CodePattern.RETURN_LIST: 0.0962,
        CodePattern.STRING_FORMAT: 0.0577,
        CodePattern.UNPACKING: 0.0577,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.4135,
        CodePattern.RETURN_NONE: 0.3365,
        CodePattern.RETURN_BOOL: 0.0769,
        CodePattern.GUARD_CLAUSE: 0.0577,
        CodePattern.IF_EMPTY_CHECK: 0.0385,
        CodePattern.LOGGING_CALL: 0.0385,
        CodePattern.TERNARY_EXPRESSION: 0.0385,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.GUARD_CLAUSE): {
        CodePattern.GUARD_CLAUSE: 0.4762,
        CodePattern.RETURN_COMPUTED: 0.3333,
        CodePattern.RETURN_NONE: 0.1905,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_FILTER: 0.6364,
        CodePattern.INIT_EMPTY_LIST: 0.3636,
    },
    (CodePattern.CLASS_METHOD, CodePattern.LIST_COMPREHENSION): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.CLASS_METHOD): {
        CodePattern.LIST_COMPREHENSION: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.7143,
        CodePattern.RETURN_COMPUTED: 0.2857,
    },
    (CodePattern.STRING_FORMAT, CodePattern.UNPACKING): {CodePattern.UNPACKING: 1.0000},
    (CodePattern.INIT_METHOD, CodePattern.CLASS_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.CLASS_METHOD, CodePattern.RETURN_COMPUTED): {
        CodePattern.CLASS_METHOD: 0.3125,
        CodePattern.FUNCTION_TRANSFORMER: 0.2500,
        CodePattern.PROPERTY_GETTER: 0.2500,
        CodePattern.IF_EMPTY_CHECK: 0.1875,
    },
    (CodePattern.STRING_FORMAT, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.STRING_FORMAT: 0.3333,
        CodePattern.FUNCTION_TRANSFORMER: 0.2222,
        CodePattern.PROPERTY_GETTER: 0.2222,
        CodePattern.RETURN_COMPUTED: 0.2222,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4000,
        CodePattern.STRING_FORMAT: 0.2000,
        CodePattern.IF_TYPE_CHECK: 0.1600,
        CodePattern.RETURN_COMPUTED: 0.1200,
        CodePattern.INIT_METHOD: 0.1200,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.RETURN_COMPUTED: 0.6250,
        CodePattern.LOOP_ACCUMULATE: 0.3750,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.7500,
        CodePattern.IF_TYPE_CHECK: 0.2500,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.6667,
        CodePattern.IF_NONE_CHECK: 0.3333,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.STRING_FORMAT): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4324,
        CodePattern.GENERATOR_EXPRESSION: 0.2432,
        CodePattern.STRING_FORMAT: 0.2162,
        CodePattern.RETURN_COMPUTED: 0.1081,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.CONTEXT_MANAGER): {
        CodePattern.CONTEXT_MANAGER: 0.3500,
        CodePattern.FUNCTION_TRANSFORMER: 0.3500,
        CodePattern.RETURN_COMPUTED: 0.3000,
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 0.2075,
        CodePattern.GUARD_CLAUSE: 0.1887,
        CodePattern.IF_NOT_NONE: 0.1509,
        CodePattern.IF_EMPTY_CHECK: 0.1321,
        CodePattern.INIT_DEFAULT_VALUE: 0.0943,
        CodePattern.TERNARY_EXPRESSION: 0.0943,
        CodePattern.RETURN_COMPUTED: 0.0755,
        CodePattern.DICT_GET_DEFAULT: 0.0566,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.LOGGING_CALL): {
        CodePattern.STRING_FORMAT: 0.6667,
        CodePattern.LOGGING_CALL: 0.3333,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.GENERATOR_EXPRESSION: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.LIST_COMPREHENSION): {
        CodePattern.LIST_COMPREHENSION: 0.5714,
        CodePattern.FUNCTION_TRANSFORMER: 0.4286,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_COMPUTED): {
        CodePattern.GUARD_CLAUSE: 0.2935,
        CodePattern.RETURN_COMPUTED: 0.2283,
        CodePattern.RETURN_NONE: 0.1739,
        CodePattern.FUNCTION_TRANSFORMER: 0.1413,
        CodePattern.RETURN_BOOL: 0.0543,
        CodePattern.STRING_FORMAT: 0.0435,
        CodePattern.INIT_METHOD: 0.0326,
        CodePattern.LOOP_ACCUMULATE: 0.0326,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.CONTEXT_MANAGER, CodePattern.STRING_FORMAT): {
        CodePattern.STRING_FORMAT: 0.7200,
        CodePattern.CONTEXT_MANAGER: 0.2800,
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.2857,
        CodePattern.FUNCTION_TRANSFORMER: 0.2143,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.IF_EMPTY_CHECK: 0.4000,
        CodePattern.LOOP_ACCUMULATE: 0.3000,
        CodePattern.RETURN_COMPUTED: 0.3000,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 0.4800,
        CodePattern.IF_NONE_CHECK: 0.2400,
        CodePattern.IF_TYPE_CHECK: 0.1600,
        CodePattern.IF_EMPTY_CHECK: 0.1200,
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 0.7895,
        CodePattern.IF_EMPTY_CHECK: 0.1316,
        CodePattern.RETURN_BOOL: 0.0789,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.3000,
        CodePattern.RETURN_COMPUTED: 0.2500,
        CodePattern.RETURN_NONE: 0.1500,
        CodePattern.IF_NOT_NONE: 0.1500,
        CodePattern.CLASS_METHOD: 0.1500,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NOT_NONE): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 0.6000,
        CodePattern.IF_EMPTY_CHECK: 0.4000,
    },
    (CodePattern.INIT_EMPTY_LIST, CodePattern.LOOP_TRANSFORM): {
        CodePattern.STRING_FORMAT: 0.5000,
        CodePattern.LOOP_ENUMERATE: 0.2500,
        CodePattern.RETURN_COMPUTED: 0.2500,
    },
    (CodePattern.STRING_FORMAT, CodePattern.INIT_EMPTY_LIST): {
        CodePattern.LOOP_TRANSFORM: 1.0000
    },
    (CodePattern.LOOP_TRANSFORM, CodePattern.STRING_FORMAT): {
        CodePattern.INIT_EMPTY_LIST: 1.0000
    },
    (CodePattern.STRING_FORMAT, CodePattern.TRY_FINALLY): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.INIT_METHOD): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOGGING_CALL, CodePattern.STRING_FORMAT): {
        CodePattern.INIT_DEFAULT_VALUE: 0.5714,
        CodePattern.STRING_FORMAT: 0.4286,
    },
    (CodePattern.LIST_COMPREHENSION, CodePattern.LOGGING_CALL): {
        CodePattern.LIST_COMPREHENSION: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5769,
        CodePattern.IF_EMPTY_CHECK: 0.1923,
        CodePattern.IF_TYPE_CHECK: 0.1154,
        CodePattern.GUARD_CLAUSE: 0.1154,
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.4194,
        CodePattern.RETURN_NONE: 0.1935,
        CodePattern.RETURN_COMPUTED: 0.1613,
        CodePattern.IF_TYPE_CHECK: 0.1290,
        CodePattern.GUARD_CLAUSE: 0.0968,
    },
    (CodePattern.RETURN_NONE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.GUARD_CLAUSE: 0.2750,
        CodePattern.RETURN_COMPUTED: 0.1500,
        CodePattern.FUNCTION_TRANSFORMER: 0.1250,
        CodePattern.IF_EMPTY_CHECK: 0.1250,
        CodePattern.DICT_GET_DEFAULT: 0.1000,
        CodePattern.IF_NOT_NONE: 0.0750,
        CodePattern.IF_TYPE_CHECK: 0.0750,
        CodePattern.RETURN_NONE: 0.0750,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LOOP_FILTER, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_BOOL): {
        CodePattern.FUNCTION_TRANSFORMER: 0.8571,
        CodePattern.RETURN_COMPUTED: 0.1429,
    },
    (CodePattern.LOOP_ACCUMULATE, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.TERNARY_EXPRESSION: 0.5000,
        CodePattern.GUARD_CLAUSE: 0.5000,
    },
    (CodePattern.LOOP_ENUMERATE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.LOOP_FILTER, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.CLASS_METHOD): {
        CodePattern.RETURN_COMPUTED: 0.7857,
        CodePattern.IF_NONE_CHECK: 0.2143,
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.IF_NONE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_FILTER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.IF_NONE_CHECK): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.INIT_DEFAULT_VALUE): {
        CodePattern.INIT_METHOD: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.LOOP_ENUMERATE): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.PROPERTY_GETTER): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.LOGGING_CALL): {
        CodePattern.STRING_FORMAT: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_NONE: 0.3200,
        CodePattern.RETURN_BOOL: 0.2800,
        CodePattern.GUARD_CLAUSE: 0.2400,
        CodePattern.RETURN_COMPUTED: 0.1600,
    },
    (CodePattern.RETURN_NONE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_NONE: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_NONE: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.IF_TYPE_CHECK): {
        CodePattern.IF_TYPE_CHECK: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_BOOL): {
        CodePattern.GUARD_CLAUSE: 0.3333,
        CodePattern.IF_EMPTY_CHECK: 0.3333,
        CodePattern.RETURN_BOOL: 0.3333,
    },
    (CodePattern.RETURN_BOOL, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_BOOL): {
        CodePattern.GUARD_CLAUSE: 0.4694,
        CodePattern.RETURN_BOOL: 0.2449,
        CodePattern.RETURN_COMPUTED: 0.1224,
        CodePattern.IF_EMPTY_CHECK: 0.0816,
        CodePattern.FUNCTION_TRANSFORMER: 0.0816,
    },
    (CodePattern.TERNARY_EXPRESSION, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_BOOL, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.RETURN_BOOL): {
        CodePattern.RETURN_BOOL: 0.6250,
        CodePattern.GUARD_CLAUSE: 0.3750,
    },
    (CodePattern.RETURN_BOOL, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.IF_NOT_NONE, CodePattern.IF_NOT_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.LOOP_FILTER, CodePattern.IF_TYPE_CHECK): {
        CodePattern.RETURN_COMPUTED: 0.5000,
        CodePattern.IF_TYPE_CHECK: 0.5000,
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.RETURN_NONE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_NONE: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.INIT_DEFAULT_VALUE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_NONE: 1.0000
    },
    (CodePattern.TRY_EXCEPT_PASS, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.TRY_EXCEPT_RERAISE): {
        CodePattern.RETURN_COMPUTED: 0.7273,
        CodePattern.IF_EMPTY_CHECK: 0.2727,
    },
    (CodePattern.RETURN_NONE, CodePattern.IF_NOT_NONE): {
        CodePattern.IF_NOT_NONE: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.FUNCTION_TRANSFORMER): {
        CodePattern.GUARD_CLAUSE: 0.5000,
        CodePattern.RETURN_COMPUTED: 0.5000,
    },
    (CodePattern.FUNCTION_TRANSFORMER, CodePattern.EARLY_RETURN_SUCCESS): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.EARLY_RETURN_SUCCESS, CodePattern.RETURN_COMPUTED): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.FUNCTION_VALIDATOR, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.RETURN_NONE: 0.6250,
        CodePattern.GUARD_CLAUSE: 0.3750,
    },
    (CodePattern.GENERATOR_EXPRESSION, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 0.6667,
        CodePattern.RETURN_COMPUTED: 0.3333,
    },
    (CodePattern.IF_NOT_NONE, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_NONE: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.RETURN_BOOL): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.GENERATOR_EXPRESSION): {
        CodePattern.RETURN_BOOL: 1.0000
    },
    (CodePattern.IF_EMPTY_CHECK, CodePattern.IF_NOT_NONE): {
        CodePattern.IF_EMPTY_CHECK: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.IF_EMPTY_CHECK): {
        CodePattern.INIT_DEFAULT_VALUE: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.UNPACKING): {
        CodePattern.IF_EMPTY_CHECK: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.RETURN_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.PROPERTY_GETTER, CodePattern.RETURN_NONE): {
        CodePattern.PROPERTY_GETTER: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_LIST: 1.0000
    },
    (CodePattern.RETURN_LIST, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.TRY_EXCEPT_RERAISE, CodePattern.RETURN_COMPUTED): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.IF_TYPE_CHECK, CodePattern.GUARD_CLAUSE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.IF_NONE_CHECK, CodePattern.CLASS_METHOD): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.INIT_METHOD, CodePattern.FUNCTION_VALIDATOR): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.UNPACKING, CodePattern.LOOP_ACCUMULATE): {
        CodePattern.LOOP_ACCUMULATE: 1.0000
    },
    (CodePattern.DICT_GET_DEFAULT, CodePattern.IF_NOT_NONE): {
        CodePattern.RETURN_COMPUTED: 1.0000
    },
    (CodePattern.GUARD_CLAUSE, CodePattern.RETURN_LIST): {
        CodePattern.GUARD_CLAUSE: 1.0000
    },
    (CodePattern.TRY_FINALLY, CodePattern.IF_NOT_NONE): {
        CodePattern.FUNCTION_TRANSFORMER: 1.0000
    },
    (CodePattern.RETURN_COMPUTED, CodePattern.EARLY_RETURN_SUCCESS): {
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
UNIQUE_SEQUENCES = 211
MIN_COUNT_THRESHOLD = 3
TOTAL_PATTERNS_TRAINED = 8062
