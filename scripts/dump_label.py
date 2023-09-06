#!/usr/bin/env python

"""
CLI helper script to create label config
in either json or yaml format
"""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import json
import logging
import os
from dataclasses import dataclass
from logging.config import fileConfig

import yaml

fileConfig("logging.ini")


@dataclass(frozen=True)
class LABELS:
    _REMOVE: tuple[str, ...] = (
        "bug",
        "dependencies",
        "documentation",
        "duplicate",
        "enhancement",
        "github_actions",
        "help wanted",
        "invalid",
        "python",
        "question",
        "wontfix",
    )
    DEFAULT: tuple[dict[str, str], ...] = (
        {
            "name": "good first issue",
            "color": "#7057ff",
            "description": "Good for newcomers.",
        },
    )
    PRIORITY: tuple[dict[str, str], ...] = (
        {
            "name": "Priority: Critical",
            "color": "#7c0a02",
        },
        {
            "name": "Priority: High",
            "color": "#b22222",
        },
        {
            "name": "Priority: Medium",
            "color": "#ff8597",
        },
        {
            "name": "Priority: Low",
            "color": "#ffccc9",
        },
    )
    TYPE: tuple[dict[str, str], ...] = (
        {
            "name": "Type: Bug",
            "color": "#ff9900",
            "description": "Something isn't working.",
        },
        {
            "name": "Type: Documentation",
            "color": "#ff9900",
            "description": "Improvements or additions to documentation.",
        },
        {
            "name": "Type: Feature Request",
            "color": "#ff9900",
            "description": "Issue describes a feature or enhancement we'd like to implement.",
        },
        {
            "name": "Type: Question",
            "color": "#ff9900",
            "description": "This issue doesn't require code. A question needs an answer.",
        },
        {
            "name": "Type: Refactor/Clean-up",
            "color": "#ff9900",
            "description": "Issues related to reorganization/clean-up of data or code (e.g. for maintainability).",
        },
        {
            "name": "Type: Suggestion",
            "color": "#ff9900",
        },
    )
    STATE: tuple[dict[str, str], ...] = (
        {
            "name": "State: Blocked",
            "color": "#e07bf9",
            "description": "Work has stopped, waiting for something (Info, Dependent fix, etc. See comments).",
        },
        {
            "name": "State: In Review",
            "color": "#e07bf9",
            "description": "This issue is waiting for review to finish.",
        },
        {
            "name": "State: Work In Progress",
            "color": "#e07bf9",
            "description": "This issue is being actively worked on.",
        },
    )
    CLOSE: tuple[dict[str, str], ...] = (
        {
            "name": "Close: Answered",
            "color": "#cdd1d5",
        },
        {
            "name": "Close: Backlog",
            "color": "#cdd1d5",
            "description": "Issues are stale/expired; sent to backlog for later re-evaluation.",
        },
        {
            "name": "Close: Duplicate",
            "color": "#cdd1d5",
            "description": "This issue or pull request already exists (see comments for pointer to it).",
        },
        {
            "name": "Close: Not Actionable",
            "color": "#cdd1d5",
        },
        {
            "name": "Close: Not Reproducible",
            "color": "#cdd1d5",
            "description": "Closed because we cannot reproduce the issue.",
        },
        {
            "name": "Close: Will Not Fix",
            "color": "#cdd1d5",
            "description": "Closed because we have decided not to address this (e.g. out of scope).",
        },
    )
    NEEDS: tuple[dict[str, str], ...] = (
        {
            "name": "Needs: Breakdown",
            "color": "#0052cc",
            "description": "This big issue needs a checklist or subissues to describe a breakdown of work.",
        },
        {
            "name": "Needs: Designs",
            "color": "#0052cc",
        },
        {
            "name": "Needs: Detail",
            "color": "#0052cc",
            "description": "Submitter needs to provide more detail for this issue to be assessed (see comments).",
        },
        {
            "name": "Needs: Feedback",
            "color": "#0052cc",
            "description": "A proposed feature or bug resolution needs feedback prior to forging ahead.",
        },
        {
            "name": "Needs: Help",
            "color": "#0052cc",
            "description": "Issues, typically substantial ones, that need a dedicated developer to take them on.",
        },
        {
            "name": "Needs: Investigation",
            "color": "#0052cc",
            "description": "This issue/PR needs a root-cause analysis to determine a solution.",
        },
        {
            "name": "Needs: Response",
            "color": "#0052cc",
            "description": "Issues which require feedback from staff members.",
        },
        {
            "name": "Needs: Review",
            "color": "#0052cc",
            "description": "This issue/PR needs to be reviewed in order to be closed or merged (see comments)",
        },
        {
            "name": "Needs: Revisiting",
            "color": "#0052cc",
            "description": "Archived (usually noisy dependencies).",
        },
        {
            "name": "Needs: Submitter Input",
            "color": "#0052cc",
            "description": "Waiting on input from the creator of the issue/pr.",
        },
        {
            "name": "Needs: Testing",
            "color": "#0052cc",
        },
        {
            "name": "Needs: Triage",
            "color": "#0052cc",
            "description": "This issue needs triage. The team needs to decide who should own it, what to do, by when.",
        },
    )
    AFFECTS: tuple[dict[str, str], ...] = (
        {
            "name": "Affects: Infra",
            "color": "#fbbc9d",
            "description": "Related to configuration, automation, CI, etc.",
        },
        {
            "name": "Affects: Project Management",
            "color": "#fbbc9d",
        },
    )


@dataclass(frozen=True)
class GAMEDEV_LABELS(LABELS):
    AFFECTS: tuple[dict[str, str], ...] = LABELS.AFFECTS + (
        {
            "name": "Affects: Game Assets",
            "color": "#fbbc9d",
            "description": "Issues relating directly to art and game assets.",
        },
        {
            "name": "Affects: Game Logic/Controls",
            "color": "#fbbc9d",
            "description": "Issues relating directly to game logic and controls.",
        },
        {
            "name": "Affects: Game Performance",
            "color": "#fbbc9d",
            "description": "Issues relating directly to squeezing game performance.",
        },
        {
            "name": "Affects: Game Rendering",
            "color": "#fbbc9d",
            "description": "Issues relating directly to game rendering.",
        },
        {
            "name": "Affects: Player Experience",
            "color": "#fbbc9d",
            "description": "Issues relating directly to game design & player experience.",
        },
    )


class DumpLabel:
    def __init__(self, dir: str = "labels", init: bool = False) -> None:
        self._dir = dir
        self._init = init

    @property
    def dir(self) -> str:
        return self._dir

    @property
    def init(self) -> bool:
        return self._init

    def _get_label_cls(self, app: str) -> LABELS:
        if app == "game":
            return GAMEDEV_LABELS()
        return LABELS()

    def _init_dir(self) -> None:
        logging.info(f"Initializing {self.dir} dir.")
        for filename in os.listdir(self.dir):
            file_path: str = os.path.join(self.dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def dump_labels(self, init: bool = False, ext: str = "yaml", app: str = "") -> None:
        if init:
            self._init_dir()

        label_cls: LABELS = self._get_label_cls(app)

        for field in label_cls.__dataclass_fields__:
            labels: tuple[dict[str, str], ...] | tuple[str, ...] = getattr(
                label_cls, field
            )
            label_file: str = os.path.join(self.dir, f"{field.lower()}_labels.{ext}")

            with open(label_file, "w+") as f:
                logging.info(f"Dumping to {f.name}.")

                if ext == "yaml":
                    print(
                        yaml.dump(
                            data=list(labels),
                            default_flow_style=False,
                            sort_keys=False,
                        ),
                        file=f,
                    )
                elif ext == "json":
                    json.dump(labels, f, indent=2)

        logging.info("Finished dumping of labels.")


def main() -> None:
    dump_label = DumpLabel()
    dump_label.dump_labels(init=True)


if __name__ == "__main__":
    main()
