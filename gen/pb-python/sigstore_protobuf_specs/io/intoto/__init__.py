# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envelope.proto
# plugin: python-betterproto
# This file has been @generated

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from dataclasses import dataclass
else:
    from pydantic.dataclasses import dataclass

from typing import List

import betterproto
from pydantic.dataclasses import rebuild_dataclass


@dataclass(eq=False, repr=False)
class Envelope(betterproto.Message):
    """An authenticated message of arbitrary type."""

    payload: bytes = betterproto.bytes_field(1)
    """
    Message to be signed. (In JSON, this is encoded as base64.)
     REQUIRED.
    """

    payload_type: str = betterproto.string_field(2)
    """
    String unambiguously identifying how to interpret payload.
     REQUIRED.
    """

    signatures: List["Signature"] = betterproto.message_field(3)
    """
    Signature over:
         PAE(type, payload)
     Where PAE is defined as:
     PAE(type, payload) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(payload) + SP + payload
     +               = concatenation
     SP              = ASCII space [0x20]
     "DSSEv1"        = ASCII [0x44, 0x53, 0x53, 0x45, 0x76, 0x31]
     LEN(s)          = ASCII decimal encoding of the byte length of s, with no leading zeros
     REQUIRED (length >= 1).
    """


@dataclass(eq=False, repr=False)
class Signature(betterproto.Message):
    sig: bytes = betterproto.bytes_field(1)
    """
    Signature itself. (In JSON, this is encoded as base64.)
     REQUIRED.
    """

    keyid: str = betterproto.string_field(2)
    """
    *Unauthenticated* hint identifying which public key was used.
     OPTIONAL.
    """


rebuild_dataclass(Envelope)  # type: ignore
