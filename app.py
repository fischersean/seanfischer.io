#!/usr/bin/env python3

from aws_cdk import core

from seanfischerio.seanfischerio_stack import SeanfischerIoStack


app = core.App()
SeanfischerIoStack(app, "seanfischer-io")

app.synth()
