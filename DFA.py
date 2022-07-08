# https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/

# https://assets.leetcode-cn.com/solution-static/jianzhi_20/jianzhi_20_fig1.png

# FIXME: 有限状态机 DFA
# https://www.zhihu.com/question/22743960

from enum import Enum

State = Enum(
    "State",
    [
        "STATE_INITIAL",
        "STATE_INT_SIGN",
        "STATE_INTEGER",
        "STATE_POINT",
        "STATE_POINT_WITHOUT_INT",
        "STATE_FRACTION",
        "STATE_EXP",
        "STATE_EXP_SIGN",
        "STATE_EXP_NUMBER",
        "STATE_END",
    ],
)
Chartype = Enum(
    "Chartype",
    [
        "CHAR_NUMBER",
        "CHAR_EXP",
        "CHAR_POINT",
        "CHAR_SIGN",
        "CHAR_SPACE",
        "CHAR_ILLEGAL",
    ],
)

TRANSFER_DICT = {
    State.STATE_INITIAL: {
        Chartype.CHAR_SPACE: State.STATE_INITIAL,
        Chartype.CHAR_NUMBER: State.STATE_INTEGER,
        Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
        Chartype.CHAR_SIGN: State.STATE_INT_SIGN,
    },
    State.STATE_INT_SIGN: {
        Chartype.CHAR_NUMBER: State.STATE_INTEGER,
        Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
    },
    State.STATE_INTEGER: {
        Chartype.CHAR_NUMBER: State.STATE_INTEGER,
        Chartype.CHAR_EXP: State.STATE_EXP,
        Chartype.CHAR_POINT: State.STATE_POINT,
        Chartype.CHAR_SPACE: State.STATE_END,
    },
    State.STATE_POINT: {
        Chartype.CHAR_NUMBER: State.STATE_FRACTION,
        Chartype.CHAR_EXP: State.STATE_EXP,
        Chartype.CHAR_SPACE: State.STATE_END,
    },
    State.STATE_POINT_WITHOUT_INT: {Chartype.CHAR_NUMBER: State.STATE_FRACTION},
    State.STATE_FRACTION: {
        Chartype.CHAR_NUMBER: State.STATE_FRACTION,
        Chartype.CHAR_EXP: State.STATE_EXP,
        Chartype.CHAR_SPACE: State.STATE_END,
    },
    State.STATE_EXP: {
        Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
        Chartype.CHAR_SIGN: State.STATE_EXP_SIGN,
    },
    State.STATE_EXP_SIGN: {Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER},
    State.STATE_EXP_NUMBER: {
        Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
        Chartype.CHAR_SPACE: State.STATE_END,
    },
    State.STATE_END: {Chartype.CHAR_SPACE: State.STATE_END},
}
