# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: producer.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'producer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproducer.proto\x12\x04jrpc\"\x90\x01\n\x0eProduceRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x32\n\x07headers\x18\x03 \x03(\x0b\x32!.jrpc.ProduceRequest.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x0fProduceResponse\x12\r\n\x05\x62ytes\x18\x01 \x01(\x04\x12\x0f\n\x07message\x18\x02 \x01(\t2D\n\x08Producer\x12\x38\n\x07Produce\x12\x14.jrpc.ProduceRequest\x1a\x15.jrpc.ProduceResponse\"\x00\x42\x08Z\x06./jrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'producer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\006./jrpc'
  _globals['_PRODUCEREQUEST_HEADERSENTRY']._loaded_options = None
  _globals['_PRODUCEREQUEST_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_PRODUCEREQUEST']._serialized_start=25
  _globals['_PRODUCEREQUEST']._serialized_end=169
  _globals['_PRODUCEREQUEST_HEADERSENTRY']._serialized_start=123
  _globals['_PRODUCEREQUEST_HEADERSENTRY']._serialized_end=169
  _globals['_PRODUCERESPONSE']._serialized_start=171
  _globals['_PRODUCERESPONSE']._serialized_end=220
  _globals['_PRODUCER']._serialized_start=222
  _globals['_PRODUCER']._serialized_end=290
# @@protoc_insertion_point(module_scope)
