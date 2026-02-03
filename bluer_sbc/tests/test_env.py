from bluer_options.testing import (
    are_01,
    are_bools,
    are_ints,
    are_positive_floats,
    are_positive_ints,
    are_nonempty_strs,
)
from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_sbc import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_blue_plugin_env():
    assert are_01(
        [
            env.BLUER_SBC_AUDIO_ENABLED,
            env.BLUER_SBC_CAMERA_FORCE_GENERIC,
            env.BLUER_SBC_CAMERA_KEEP_OPEN,
            env.BLUER_SBC_DISPLAY_FULLSCREEN,
            env.BLUER_SBC_SWALLOW_DEV_MODE,
            env.BLUER_SBC_SWALLOW_HAS_BPS,
            env.BLUER_SBC_SWALLOW_HAS_CAMERA,
            env.BLUER_SBC_SWALLOW_HAS_FULL_KEYBOARD,
            env.BLUER_SBC_SWALLOW_HAS_STEERING,
        ]
    )

    assert are_bools(
        [
            env.BLUER_SBC_CAMERA_HI_RES,
            env.BLUER_SBC_SESSION_AUTO_UPLOAD,
            env.BLUER_SBC_SESSION_IMAGER_ENABLED,
            env.BLUER_SBC_SESSION_MONITOR_ENABLED,
        ]
    )

    assert are_positive_floats(
        [
            env.BLUER_SBC_SESSION_IMAGER_DIFF,
        ]
    )

    assert are_ints(
        [
            env.BLUER_SBC_CAMERA_ROTATION,
        ]
    )

    assert are_positive_ints(
        [
            env.BLUER_SBC_CAMERA_HEIGHT,
            env.BLUER_SBC_CAMERA_WIDTH,
            env.BLUER_SBC_SESSION_IMAGER_PERIOD,
            env.BLUER_SBC_SESSION_MESSENGER_PERIOD,
            env.BLUER_SBC_SESSION_REBOOT_PERIOD,
            env.BLUER_SBC_SESSION_SCREEN_PERIOD,
            env.BLUER_SBC_SESSION_TEMPERATURE_PERIOD,
        ]
    )

    assert are_nonempty_strs(
        [
            env.BLUER_SBC_BPS_ANCHORED_AT,
            env.BLUER_SBC_CAMERA_KIND,
            env.BLUER_SBC_HARDWARE_KIND,
            env.BLUER_SBC_SESSION_IMAGER,
            env.BLUER_SBC_SESSION_OBJECT_TAGS,
            env.BLUER_SBC_SESSION_OUTBOUND_QUEUE,
            env.BLUER_SBC_SESSION_PLUGIN,
        ]
    )
