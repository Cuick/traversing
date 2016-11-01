# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import player_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='',
  serialized_pb='\n\ngame.proto\x1a\x0c\x63ommon.proto\x1a\x0cplayer.proto\"\x8b\x04\n\x10GameLoginRequest\x12\r\n\x05token\x18\x01 \x02(\t\x12\x0f\n\x07plat_id\x18\x02 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x03 \x01(\t\x12\x17\n\x0fsystem_software\x18\x04 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\x05 \x01(\t\x12\x14\n\x0ctelecom_oper\x18\x06 \x01(\t\x12\x0f\n\x07network\x18\x07 \x01(\t\x12\x14\n\x0cscreen_width\x18\x08 \x01(\x05\x12\x14\n\x0cscreen_hight\x18\t \x01(\x05\x12\x0f\n\x07\x64\x65nsity\x18\n \x01(\x02\x12\x15\n\rlogin_channel\x18\x0b \x01(\t\x12\x0b\n\x03mac\x18\x0c \x01(\t\x12\x14\n\x0c\x63pu_hardware\x18\r \x01(\t\x12\x0e\n\x06memory\x18\x0e \x01(\x05\x12\x11\n\tgl_render\x18\x0f \x01(\t\x12\x12\n\ngl_version\x18\x10 \x01(\t\x12\x11\n\tdevice_id\x18\x11 \x01(\t\x12\x10\n\x08platform\x18\x12 \x01(\x05\x12\x0f\n\x07open_id\x18\x13 \x01(\t\x12\x10\n\x08open_key\x18\x14 \x01(\t\x12\x11\n\tpay_token\x18\x15 \x01(\t\x12\r\n\x05\x61ppid\x18\x16 \x01(\t\x12\x0e\n\x06\x61ppkey\x18\x1a \x01(\t\x12\n\n\x02pf\x18\x17 \x01(\t\x12\r\n\x05pfkey\x18\x18 \x01(\t\x12\x0e\n\x06zoneid\x18\x19 \x01(\t\x12\x13\n\x0brecharge_id\x18\x1b \x01(\x05\"\xc1\x08\n\x11GameLoginResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x05 \x01(\x05\x12\x10\n\x08\x66inances\x18\x06 \x03(\x05\x12\x11\n\tfine_hero\x18\x07 \x01(\x05\x12\x16\n\x0e\x65xcellent_hero\x18\x08 \x01(\x05\x12\x16\n\x0e\x66ine_equipment\x18\t \x01(\x05\x12\x1b\n\x13\x65xcellent_equipment\x18\n \x01(\x05\x12\x11\n\tpvp_times\x18\x0b \x01(\x05\x12\x19\n\x11pvp_refresh_count\x18\x0c \x01(\x05\x12\x11\n\tvip_level\x18\r \x01(\x05\x12\x13\n\x0bserver_time\x18\x0e \x01(\x05\x12\x10\n\x08guild_id\x18\x0f \x01(\x05\x12\x14\n\x0c\x63ombat_power\x18\x10 \x01(\x02\x12\x17\n\x0fnewbee_guide_id\x18\x11 \x01(\x05\x12\x15\n\rregister_time\x18\x18 \x01(\x05\x12\x19\n\x11get_stamina_times\x18\x12 \x01(\x05\x12\x19\n\x11\x62uy_stamina_times\x18\x13 \x01(\x05\x12\x1e\n\x16last_gain_stamina_time\x18\x14 \x01(\x05\x12\x1f\n\x17soul_shop_refresh_times\x18\x15 \x01(\x05\x12\x0c\n\x04head\x18\x16 \x03(\x05\x12\x10\n\x08now_head\x18\x17 \x01(\x05\x12\x1a\n\x12\x66irst_recharge_ids\x18\x19 \x03(\x05\x12\x0b\n\x03gag\x18\x1a \x01(\x05\x12\x0f\n\x07\x63losure\x18\x1b \x01(\x05\x12\x10\n\x08recharge\x18\x1c \x01(\x05\x12\x15\n\rtomorrow_gift\x18\x1d \x01(\x05\x12\x14\n\x0c\x62\x61ttle_speed\x18\x1e \x01(\x05\x12\x17\n\x0f\x66ine_hero_times\x18\x1f \x01(\x05\x12\x1c\n\x14\x65xcellent_hero_times\x18  \x01(\x05\x12\x18\n\x10\x66ight_power_rank\x18! \x01(\x05\x12\x1a\n\x12pvp_overcome_index\x18\" \x01(\x05\x12\x1a\n\x12pvp_overcome_stars\x18$ \x01(\x05\x12\"\n\x1apvp_overcome_refresh_count\x18% \x01(\x05\x12#\n\tbuy_times\x18& \x03(\x0b\x32\x10.BuyStaminaTimes\x12!\n\x19is_open_next_day_activity\x18\' \x01(\x08\x12\x1f\n\x17\x66irst_recharge_activity\x18( \x01(\x05\x12\x13\n\x0bhight_power\x18) \x01(\x02\x12\x10\n\x08story_id\x18* \x01(\x05\x12\x17\n\x0f\x62utton_one_time\x18+ \x03(\x05\x12\x18\n\x10server_open_time\x18, \x01(\x05\x12\x19\n\x11q360_recharge_url\x18- \x01(\t\x12\x19\n\x11one_dollar_flowid\x18. \x01(\t\"c\n\x0f\x42uyStaminaTimes\x12\x15\n\rresource_type\x18\x01 \x01(\x05\x12\x19\n\x11\x62uy_stamina_times\x18\x02 \x01(\x05\x12\x1e\n\x16last_gain_stamina_time\x18\x03 \x01(\x05\"(\n\x11HeartBeatResponse\x12\x13\n\x0bserver_time\x18\x01 \x01(\x05\">\n\x12StaminaOperRequest\x12(\n\x0f\x66inance_changes\x18\x02 \x02(\x0b\x32\x0f.FinanceChanges\"p\n\x13StaminaOperResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12(\n\x0f\x66inance_changes\x18\x02 \x02(\x0b\x32\x0f.FinanceChanges\x12\x11\n\tbuy_times\x18\x03 \x01(\x05')




_GAMELOGINREQUEST = _descriptor.Descriptor(
  name='GameLoginRequest',
  full_name='GameLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='GameLoginRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plat_id', full_name='GameLoginRequest.plat_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='GameLoginRequest.client_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_software', full_name='GameLoginRequest.system_software', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_hardware', full_name='GameLoginRequest.system_hardware', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='telecom_oper', full_name='GameLoginRequest.telecom_oper', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='network', full_name='GameLoginRequest.network', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screen_width', full_name='GameLoginRequest.screen_width', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screen_hight', full_name='GameLoginRequest.screen_hight', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='density', full_name='GameLoginRequest.density', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_channel', full_name='GameLoginRequest.login_channel', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac', full_name='GameLoginRequest.mac', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_hardware', full_name='GameLoginRequest.cpu_hardware', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory', full_name='GameLoginRequest.memory', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gl_render', full_name='GameLoginRequest.gl_render', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gl_version', full_name='GameLoginRequest.gl_version', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='GameLoginRequest.device_id', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform', full_name='GameLoginRequest.platform', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_id', full_name='GameLoginRequest.open_id', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_key', full_name='GameLoginRequest.open_key', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pay_token', full_name='GameLoginRequest.pay_token', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appid', full_name='GameLoginRequest.appid', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appkey', full_name='GameLoginRequest.appkey', index=22,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pf', full_name='GameLoginRequest.pf', index=23,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pfkey', full_name='GameLoginRequest.pfkey', index=24,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zoneid', full_name='GameLoginRequest.zoneid', index=25,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recharge_id', full_name='GameLoginRequest.recharge_id', index=26,
      number=27, type=5, cpp_type=1, label=1,
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
  serialized_start=43,
  serialized_end=566,
)


_GAMELOGINRESPONSE = _descriptor.Descriptor(
  name='GameLoginResponse',
  full_name='GameLoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='GameLoginResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='GameLoginResponse.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='GameLoginResponse.nickname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GameLoginResponse.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='GameLoginResponse.exp', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finances', full_name='GameLoginResponse.finances', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_hero', full_name='GameLoginResponse.fine_hero', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_hero', full_name='GameLoginResponse.excellent_hero', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_equipment', full_name='GameLoginResponse.fine_equipment', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_equipment', full_name='GameLoginResponse.excellent_equipment', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_times', full_name='GameLoginResponse.pvp_times', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_refresh_count', full_name='GameLoginResponse.pvp_refresh_count', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='GameLoginResponse.vip_level', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='GameLoginResponse.server_time', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='GameLoginResponse.guild_id', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_power', full_name='GameLoginResponse.combat_power', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newbee_guide_id', full_name='GameLoginResponse.newbee_guide_id', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register_time', full_name='GameLoginResponse.register_time', index=17,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_stamina_times', full_name='GameLoginResponse.get_stamina_times', index=18,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_stamina_times', full_name='GameLoginResponse.buy_stamina_times', index=19,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_gain_stamina_time', full_name='GameLoginResponse.last_gain_stamina_time', index=20,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soul_shop_refresh_times', full_name='GameLoginResponse.soul_shop_refresh_times', index=21,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head', full_name='GameLoginResponse.head', index=22,
      number=22, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='now_head', full_name='GameLoginResponse.now_head', index=23,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_recharge_ids', full_name='GameLoginResponse.first_recharge_ids', index=24,
      number=25, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gag', full_name='GameLoginResponse.gag', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='closure', full_name='GameLoginResponse.closure', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recharge', full_name='GameLoginResponse.recharge', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tomorrow_gift', full_name='GameLoginResponse.tomorrow_gift', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_speed', full_name='GameLoginResponse.battle_speed', index=29,
      number=30, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_hero_times', full_name='GameLoginResponse.fine_hero_times', index=30,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_hero_times', full_name='GameLoginResponse.excellent_hero_times', index=31,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight_power_rank', full_name='GameLoginResponse.fight_power_rank', index=32,
      number=33, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_overcome_index', full_name='GameLoginResponse.pvp_overcome_index', index=33,
      number=34, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_overcome_stars', full_name='GameLoginResponse.pvp_overcome_stars', index=34,
      number=36, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_overcome_refresh_count', full_name='GameLoginResponse.pvp_overcome_refresh_count', index=35,
      number=37, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_times', full_name='GameLoginResponse.buy_times', index=36,
      number=38, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_open_next_day_activity', full_name='GameLoginResponse.is_open_next_day_activity', index=37,
      number=39, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_recharge_activity', full_name='GameLoginResponse.first_recharge_activity', index=38,
      number=40, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hight_power', full_name='GameLoginResponse.hight_power', index=39,
      number=41, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='story_id', full_name='GameLoginResponse.story_id', index=40,
      number=42, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='button_one_time', full_name='GameLoginResponse.button_one_time', index=41,
      number=43, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_open_time', full_name='GameLoginResponse.server_open_time', index=42,
      number=44, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q360_recharge_url', full_name='GameLoginResponse.q360_recharge_url', index=43,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='one_dollar_flowid', full_name='GameLoginResponse.one_dollar_flowid', index=44,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_end=1658,
)


_BUYSTAMINATIMES = _descriptor.Descriptor(
  name='BuyStaminaTimes',
  full_name='BuyStaminaTimes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='BuyStaminaTimes.resource_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_stamina_times', full_name='BuyStaminaTimes.buy_stamina_times', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_gain_stamina_time', full_name='BuyStaminaTimes.last_gain_stamina_time', index=2,
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
  serialized_start=1660,
  serialized_end=1759,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartBeatResponse',
  full_name='HeartBeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_time', full_name='HeartBeatResponse.server_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1761,
  serialized_end=1801,
)


_STAMINAOPERREQUEST = _descriptor.Descriptor(
  name='StaminaOperRequest',
  full_name='StaminaOperRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='finance_changes', full_name='StaminaOperRequest.finance_changes', index=0,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=1803,
  serialized_end=1865,
)


_STAMINAOPERRESPONSE = _descriptor.Descriptor(
  name='StaminaOperResponse',
  full_name='StaminaOperResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='StaminaOperResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finance_changes', full_name='StaminaOperResponse.finance_changes', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_times', full_name='StaminaOperResponse.buy_times', index=2,
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
  serialized_start=1867,
  serialized_end=1979,
)

_GAMELOGINRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_GAMELOGINRESPONSE.fields_by_name['buy_times'].message_type = _BUYSTAMINATIMES
_STAMINAOPERREQUEST.fields_by_name['finance_changes'].message_type = player_pb2._FINANCECHANGES
_STAMINAOPERRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_STAMINAOPERRESPONSE.fields_by_name['finance_changes'].message_type = player_pb2._FINANCECHANGES
DESCRIPTOR.message_types_by_name['GameLoginRequest'] = _GAMELOGINREQUEST
DESCRIPTOR.message_types_by_name['GameLoginResponse'] = _GAMELOGINRESPONSE
DESCRIPTOR.message_types_by_name['BuyStaminaTimes'] = _BUYSTAMINATIMES
DESCRIPTOR.message_types_by_name['HeartBeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['StaminaOperRequest'] = _STAMINAOPERREQUEST
DESCRIPTOR.message_types_by_name['StaminaOperResponse'] = _STAMINAOPERRESPONSE

class GameLoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINREQUEST

  # @@protoc_insertion_point(class_scope:GameLoginRequest)

class GameLoginResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINRESPONSE

  # @@protoc_insertion_point(class_scope:GameLoginResponse)

class BuyStaminaTimes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYSTAMINATIMES

  # @@protoc_insertion_point(class_scope:BuyStaminaTimes)

class HeartBeatResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEARTBEATRESPONSE

  # @@protoc_insertion_point(class_scope:HeartBeatResponse)

class StaminaOperRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAMINAOPERREQUEST

  # @@protoc_insertion_point(class_scope:StaminaOperRequest)

class StaminaOperResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAMINAOPERRESPONSE

  # @@protoc_insertion_point(class_scope:StaminaOperResponse)


# @@protoc_insertion_point(module_scope)