from bluer_sbc.README.designs import (
    adapter_bus,
    nafha,
    pwm_generator,
    regulated_bus,
    shelter,
    template,
    ultrasonic_sensor_tester,
)
from bluer_sbc.README.designs.anchor import docs as anchor
from bluer_sbc.README.designs.battery_bus import docs as battery_bus
from bluer_sbc.README.designs.cheshmak import docs as cheshmak
from bluer_sbc.README.designs.isatis import docs as isatis
from bluer_sbc.README.designs.kulej import docs as kulej
from bluer_sbc.README.designs.swallow import docs as swallow
from bluer_sbc.README.designs.swallow_head import docs as swallow_head


docs = (
    adapter_bus.docs
    + anchor.docs
    + battery_bus.docs
    + cheshmak.docs
    + isatis.docs
    + kulej.docs
    + nafha.docs
    + pwm_generator.docs
    + regulated_bus.docs
    + shelter.docs
    + swallow_head.docs
    + swallow.docs
    + ultrasonic_sensor_tester.docs
    + template.docs
)
