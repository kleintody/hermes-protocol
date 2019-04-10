# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from ..ffi import lib
from .wrappers import wrap_library_call

from ..ontology import MqttOptions

# re-exports

hermes_protocol_handler_new_mqtt = wrap_library_call(lib.hermes_protocol_handler_new_mqtt)
hermes_protocol_handler_new_mqtt_with_options = wrap_library_call(lib.hermes_protocol_handler_new_mqtt_with_options)

# dialogue
hermes_protocol_handler_dialogue_facade = wrap_library_call(lib.hermes_protocol_handler_dialogue_facade)

hermes_dialogue_subscribe_intent = wrap_library_call(lib.hermes_dialogue_subscribe_intent)
hermes_dialogue_subscribe_intents = wrap_library_call(lib.hermes_dialogue_subscribe_intents)
hermes_dialogue_subscribe_session_ended = wrap_library_call(lib.hermes_dialogue_subscribe_session_ended)
hermes_dialogue_subscribe_session_queued = wrap_library_call(lib.hermes_dialogue_subscribe_session_queued)
hermes_dialogue_subscribe_session_started = wrap_library_call(lib.hermes_dialogue_subscribe_session_started)
hermes_dialogue_subscribe_intent_not_recognized = wrap_library_call(lib.hermes_dialogue_subscribe_intent_not_recognized)

hermes_dialogue_publish_continue_session = wrap_library_call(lib.hermes_dialogue_publish_continue_session)
hermes_dialogue_publish_end_session = wrap_library_call(lib.hermes_dialogue_publish_end_session)
hermes_dialogue_publish_start_session = wrap_library_call(lib.hermes_dialogue_publish_start_session)

hermes_dialogue_publish_continue_session_json = wrap_library_call(lib.hermes_dialogue_publish_continue_session_json)
hermes_dialogue_publish_end_session_json = wrap_library_call(lib.hermes_dialogue_publish_end_session_json)
hermes_dialogue_publish_start_session_json = wrap_library_call(lib.hermes_dialogue_publish_start_session_json)
hermes_dialogue_subscribe_intent_json = wrap_library_call(lib.hermes_dialogue_subscribe_intent_json)
hermes_dialogue_subscribe_intent_not_recognized_json = \
    wrap_library_call(lib.hermes_dialogue_subscribe_intent_not_recognized_json)
hermes_dialogue_subscribe_intents_json = wrap_library_call(lib.hermes_dialogue_subscribe_intents_json)
hermes_dialogue_subscribe_session_ended_json = wrap_library_call(lib.hermes_dialogue_subscribe_session_ended_json)
hermes_dialogue_subscribe_session_queued_json = wrap_library_call(lib.hermes_dialogue_subscribe_session_queued_json)
hermes_dialogue_subscribe_session_started_json = wrap_library_call(lib.hermes_dialogue_subscribe_session_started_json)
hermes_dialogue_publish_configure = wrap_library_call(lib.hermes_dialogue_publish_configure)

# feedback
hermes_protocol_handler_sound_feedback_facade = wrap_library_call(lib.hermes_protocol_handler_sound_feedback_facade)

hermes_sound_feedback_publish_toggle_on = wrap_library_call(lib.hermes_sound_feedback_publish_toggle_on)
hermes_sound_feedback_publish_toggle_off = wrap_library_call(lib.hermes_sound_feedback_publish_toggle_off)

# injection
hermes_protocol_handler_injection_facade = wrap_library_call(lib.hermes_protocol_handler_injection_facade)

hermes_injection_publish_injection_request = wrap_library_call(lib.hermes_injection_publish_injection_request)
hermes_injection_publish_injection_status_request = wrap_library_call(
    lib.hermes_injection_publish_injection_status_request)

hermes_injection_subscribe_injection_status = wrap_library_call(lib.hermes_injection_subscribe_injection_status)

# Freeing facades
hermes_drop_asr_backend_facade = wrap_library_call(lib.hermes_drop_asr_backend_facade)
hermes_drop_asr_facade = wrap_library_call(lib.hermes_drop_asr_facade)
hermes_drop_audio_server_backend_facade = wrap_library_call(lib.hermes_drop_audio_server_backend_facade)
hermes_drop_audio_server_facade = wrap_library_call(lib.hermes_drop_audio_server_facade)
hermes_drop_dialogue_backend_facade = wrap_library_call(lib.hermes_drop_dialogue_backend_facade)
hermes_drop_dialogue_facade = wrap_library_call(lib.hermes_drop_dialogue_facade)
hermes_drop_hotword_backend_facade = wrap_library_call(lib.hermes_drop_hotword_backend_facade)
hermes_drop_hotword_facade = wrap_library_call(lib.hermes_drop_hotword_facade)
hermes_drop_nlu_backend_facade = wrap_library_call(lib.hermes_drop_nlu_backend_facade)
hermes_drop_nlu_facade = wrap_library_call(lib.hermes_drop_nlu_facade)
hermes_drop_sound_feedback_backend_facade = wrap_library_call(lib.hermes_drop_sound_feedback_backend_facade)
hermes_drop_sound_feedback_facade = wrap_library_call(lib.hermes_drop_sound_feedback_facade)
hermes_drop_tts_backend_facade = wrap_library_call(lib.hermes_drop_tts_backend_facade)
hermes_drop_tts_facade = wrap_library_call(lib.hermes_drop_tts_facade)
hermes_drop_injection_status_message = wrap_library_call(lib.hermes_drop_injection_status_message)
hermes_drop_injection_facade = wrap_library_call(lib.hermes_drop_injection_facade)