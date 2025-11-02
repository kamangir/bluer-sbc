from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_sbc import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_blue_plugin_env():
    assert isinstance(env.BLUER_SBC_CAMERA_HI_RES, bool)
    assert isinstance(env.BLUER_SBC_CAMERA_WIDTH, int)
    assert isinstance(env.BLUER_SBC_CAMERA_HEIGHT, int)
    assert isinstance(env.BLUER_SBC_CAMERA_ROTATION, int)
    assert isinstance(env.BLUER_SBC_CAMERA_KEEP_OPEN, int)

    assert isinstance(env.BLUER_SBC_DISPLAY_FULLSCREEN, bool)

    assert env.BLUER_SBC_HARDWARE_KIND

    assert isinstance(env.BLUER_SBC_SESSION_PLUGIN, str)

    assert isinstance(env.BLUER_SBC_SESSION_IMAGER, str)

    assert isinstance(env.BLUER_SBC_SESSION_IMAGER_DIFF, float)
    assert isinstance(env.BLUER_SBC_SESSION_IMAGER_ENABLED, bool)
    assert isinstance(env.BLUER_SBC_SESSION_MONITOR_ENABLED, bool)

    assert isinstance(env.BLUER_SBC_SESSION_OBJECT_TAGS, str)

    assert isinstance(env.BLUER_SBC_SESSION_OUTBOUND_QUEUE, str)

    assert isinstance(env.BLUER_SBC_SESSION_AUTO_UPLOAD, bool)

    assert isinstance(env.BLUER_SBC_SESSION_IMAGER_PERIOD, int)
    assert isinstance(env.BLUER_SBC_SESSION_MESSENGER_PERIOD, int)
    assert isinstance(env.BLUER_SBC_SESSION_REBOOT_PERIOD, int)
    assert isinstance(env.BLUER_SBC_SESSION_SCREEN_PERIOD, int)
    assert isinstance(env.BLUER_SBC_SESSION_TEMPERATURE_PERIOD, int)

    assert env.BLUER_SBC_ENV

    assert isinstance(env.BLUER_SBC_SWALLOW_HAS_STEERING, int)
    assert isinstance(env.BLUER_SBC_SWALLOW_HAS_FULL_KEYBOARD, int)
    assert isinstance(env.BLUER_SBC_SWALLOW_HAS_BPS, int)

    assert isinstance(env.BLUER_SBC_BPS_ANCHORED_AT, str)

    assert isinstance(env.BLUER_SBC_BPS_ANCHORED_AT, str)
