# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hero_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import hero_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hero_response.proto',
  package='',
  serialized_pb='\n\x13hero_response.proto\x1a\x0c\x63ommon.proto\x1a\nhero.proto\"*\n\x10GetHerosResponse\x12\x16\n\x05heros\x18\x01 \x03(\x0b\x32\x07.HeroPB\"O\n\x13HeroUpgradeResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\"\x87\x01\n\x11HeroBreakResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\'\n\x07\x63onsume\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12\x13\n\x0b\x62reak_level\x18\x03 \x01(\x05\x12\x16\n\x0e\x62reak_item_num\x18\x04 \x01(\x05\"[\n\x15HeroSacrificeResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\"J\n\x13HeroComposeResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x15\n\x04hero\x18\x02 \x01(\x0b\x32\x07.HeroPB\"V\n\x10HeroSellResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\"[\n\x12HeroRefineResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\'\n\x07\x63onsume\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\"j\n\x18OneKeyHeroUpgradeRespone\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\x12\x14\n\x0c\x65xp_item_num\x18\x04 \x03(\x05\"\x9a\x01\n\x11HeroAwakeResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x13\n\x0b\x61wake_level\x18\x02 \x01(\x05\x12\x11\n\tawake_exp\x18\x03 \x01(\x05\x12\x16\n\x0e\x61wake_item_num\x18\x04 \x01(\x05\x12\'\n\x07\x63onsume\x18\x05 \x01(\x0b\x32\x16.GameResourcesResponse\"M\n\x1cHeroBreakRelatedInfoResponse\x12\x16\n\x0e\x62reak_item_num\x18\x01 \x01(\x05\x12\x15\n\rhero_chip_num\x18\x02 \x01(\x05')




_GETHEROSRESPONSE = _descriptor.Descriptor(
  name='GetHerosResponse',
  full_name='GetHerosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heros', full_name='GetHerosResponse.heros', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=91,
)


_HEROUPGRADERESPONSE = _descriptor.Descriptor(
  name='HeroUpgradeResponse',
  full_name='HeroUpgradeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='HeroUpgradeResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='HeroUpgradeResponse.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='HeroUpgradeResponse.exp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=93,
  serialized_end=172,
)


_HEROBREAKRESPONSE = _descriptor.Descriptor(
  name='HeroBreakResponse',
  full_name='HeroBreakResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='HeroBreakResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='HeroBreakResponse.consume', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='break_level', full_name='HeroBreakResponse.break_level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='break_item_num', full_name='HeroBreakResponse.break_item_num', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=175,
  serialized_end=310,
)


_HEROSACRIFICERESPONSE = _descriptor.Descriptor(
  name='HeroSacrificeResponse',
  full_name='HeroSacrificeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='HeroSacrificeResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='HeroSacrificeResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=312,
  serialized_end=403,
)


_HEROCOMPOSERESPONSE = _descriptor.Descriptor(
  name='HeroComposeResponse',
  full_name='HeroComposeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='HeroComposeResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero', full_name='HeroComposeResponse.hero', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=405,
  serialized_end=479,
)


_HEROSELLRESPONSE = _descriptor.Descriptor(
  name='HeroSellResponse',
  full_name='HeroSellResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='HeroSellResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='HeroSellResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=481,
  serialized_end=567,
)


_HEROREFINERESPONSE = _descriptor.Descriptor(
  name='HeroRefineResponse',
  full_name='HeroRefineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='HeroRefineResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='HeroRefineResponse.consume', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=569,
  serialized_end=660,
)


_ONEKEYHEROUPGRADERESPONE = _descriptor.Descriptor(
  name='OneKeyHeroUpgradeRespone',
  full_name='OneKeyHeroUpgradeRespone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='OneKeyHeroUpgradeRespone.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='OneKeyHeroUpgradeRespone.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='OneKeyHeroUpgradeRespone.exp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp_item_num', full_name='OneKeyHeroUpgradeRespone.exp_item_num', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=662,
  serialized_end=768,
)


_HEROAWAKERESPONSE = _descriptor.Descriptor(
  name='HeroAwakeResponse',
  full_name='HeroAwakeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='HeroAwakeResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awake_level', full_name='HeroAwakeResponse.awake_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awake_exp', full_name='HeroAwakeResponse.awake_exp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awake_item_num', full_name='HeroAwakeResponse.awake_item_num', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consume', full_name='HeroAwakeResponse.consume', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=771,
  serialized_end=925,
)


_HEROBREAKRELATEDINFORESPONSE = _descriptor.Descriptor(
  name='HeroBreakRelatedInfoResponse',
  full_name='HeroBreakRelatedInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='break_item_num', full_name='HeroBreakRelatedInfoResponse.break_item_num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_chip_num', full_name='HeroBreakRelatedInfoResponse.hero_chip_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=927,
  serialized_end=1004,
)

_GETHEROSRESPONSE.fields_by_name['heros'].message_type = hero_pb2._HEROPB
_HEROUPGRADERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROBREAKRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROBREAKRESPONSE.fields_by_name['consume'].message_type = common_pb2._GAMERESOURCESRESPONSE
_HEROSACRIFICERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROSACRIFICERESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_HEROCOMPOSERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROCOMPOSERESPONSE.fields_by_name['hero'].message_type = hero_pb2._HEROPB
_HEROSELLRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROSELLRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_HEROREFINERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROREFINERESPONSE.fields_by_name['consume'].message_type = common_pb2._GAMERESOURCESRESPONSE
_ONEKEYHEROUPGRADERESPONE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROAWAKERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_HEROAWAKERESPONSE.fields_by_name['consume'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['GetHerosResponse'] = _GETHEROSRESPONSE
DESCRIPTOR.message_types_by_name['HeroUpgradeResponse'] = _HEROUPGRADERESPONSE
DESCRIPTOR.message_types_by_name['HeroBreakResponse'] = _HEROBREAKRESPONSE
DESCRIPTOR.message_types_by_name['HeroSacrificeResponse'] = _HEROSACRIFICERESPONSE
DESCRIPTOR.message_types_by_name['HeroComposeResponse'] = _HEROCOMPOSERESPONSE
DESCRIPTOR.message_types_by_name['HeroSellResponse'] = _HEROSELLRESPONSE
DESCRIPTOR.message_types_by_name['HeroRefineResponse'] = _HEROREFINERESPONSE
DESCRIPTOR.message_types_by_name['OneKeyHeroUpgradeRespone'] = _ONEKEYHEROUPGRADERESPONE
DESCRIPTOR.message_types_by_name['HeroAwakeResponse'] = _HEROAWAKERESPONSE
DESCRIPTOR.message_types_by_name['HeroBreakRelatedInfoResponse'] = _HEROBREAKRELATEDINFORESPONSE

class GetHerosResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHEROSRESPONSE

  # @@protoc_insertion_point(class_scope:GetHerosResponse)

class HeroUpgradeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROUPGRADERESPONSE

  # @@protoc_insertion_point(class_scope:HeroUpgradeResponse)

class HeroBreakResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROBREAKRESPONSE

  # @@protoc_insertion_point(class_scope:HeroBreakResponse)

class HeroSacrificeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROSACRIFICERESPONSE

  # @@protoc_insertion_point(class_scope:HeroSacrificeResponse)

class HeroComposeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROCOMPOSERESPONSE

  # @@protoc_insertion_point(class_scope:HeroComposeResponse)

class HeroSellResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROSELLRESPONSE

  # @@protoc_insertion_point(class_scope:HeroSellResponse)

class HeroRefineResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROREFINERESPONSE

  # @@protoc_insertion_point(class_scope:HeroRefineResponse)

class OneKeyHeroUpgradeRespone(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONEKEYHEROUPGRADERESPONE

  # @@protoc_insertion_point(class_scope:OneKeyHeroUpgradeRespone)

class HeroAwakeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROAWAKERESPONSE

  # @@protoc_insertion_point(class_scope:HeroAwakeResponse)

class HeroBreakRelatedInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEROBREAKRELATEDINFORESPONSE

  # @@protoc_insertion_point(class_scope:HeroBreakRelatedInfoResponse)


# @@protoc_insertion_point(module_scope)
