STYLES = {
    "dramatic": {
        "intros": [
            "In a shocking turn,",
            "Against all odds,",
            "Meanwhile,",
            "In a twist no one expected,",
            "With dramatic flair,",
        ],
        "emphasis": [
            "dramatically",
            "with thunderous gravitas",
            "as the suspense mounted",
            "under a stormy sky",
            "to the sound of distant keyboards",
        ],
        "cliffhangers": [
            "Will the action items survive the week?",
            "Can the blockers be unblocked in time?",
            "Find out in the next standup!",
        ],
    },
    "snarky": {
        "intros": [
            "Plot twist:",
            "As if things weren't spicy,",
            "Cue the side-eye,",
            "In the latest episode,",
            "Somehow,",
        ],
        "emphasis": [
            "with a side of eye-roll",
            "while pretending to be surprised",
            "as the coffee ran low",
            "with suspicious enthusiasm",
            "as everyone nodded knowingly",
        ],
        "cliffhangers": [
            "Will the calendar invite strike again?",
            "Can anyone find the parking lot?",
            "Tune in after the next 'quick sync'!",
        ],
    },
    "neutral": {
        "intros": [
            "Notably,",
            "Additionally,",
            "It was noted that",
            "To summarize,",
            "For reference,",
        ],
        "emphasis": [
            "for the record",
            "as documented",
            "with consensus",
            "as agreed",
            "without further drama",
        ],
        "cliffhangers": [
            "Next steps will be shared soon.",
            "Action items have been captured for follow-up.",
            "Updates will continue at the next meeting.",
        ],
    },
}

INTROS = STYLES["dramatic"]["intros"]
EMPHASIS = STYLES["dramatic"]["emphasis"]
CLIFFHANGERS = STYLES["dramatic"]["cliffhangers"]

ACTION_KEYWORDS = [
    "action",
    "todo",
    "to-do",
    "follow up",
    "follow-up",
    "owner",
    "next step",
    "due",
]
