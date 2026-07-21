from enum import Enum


class AgentState(str, Enum):

    START = "START"

    INTAKE = "INTAKE"

    SEARCH = "SEARCH"

    DIAGNOSIS = "DIAGNOSIS"

    PATCH = "PATCH"

    TEST = "TEST"

    REPORT = "REPORT"

    END = "END"