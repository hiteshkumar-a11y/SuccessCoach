from src.student_data.google_sheet_service import signal_sheet

from src.planning.planner_service import (
    create_plan
)


def generate_daily_plan():

    signals = signal_sheet.get_all_records()

    active_signals = []

    for signal in signals:

        if (
            str(
                signal.get(
                    "actioned",
                    ""
                )
            ).upper()
            != "TRUE"
        ):

            active_signals.append(
                signal
            )

    if not active_signals:

        return {
            "today": [],
            "deferred": []
        }

    return create_plan(
        active_signals
    )