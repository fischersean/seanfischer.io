#!/usr/bin/env python3

from aws_cdk import core

from seanfischer.io.seanfischer.io_stack import SeanfischerIoStack


app = core.App()
SeanfischerIoStack(app, "seanfischer-io")

app.synth()
