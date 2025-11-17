from bluer_sbc.README.designs import (
    adapter_bus,
    battery_bus,
    bryce,
    cheshmak,
    nafha,
    pwm_generator,
    regulated_bus,
    shelter,
    swallow_head,
    template,
    ultrasonic_sensor_tester,
)
from bluer_sbc.README.designs.swallow import docs as swallow


docs = (
    adapter_bus.docs
    + battery_bus.docs
    + bryce.docs
    + cheshmak.docs
    + nafha.docs
    + pwm_generator.docs
    + regulated_bus.docs
    + shelter.docs
    + swallow_head.docs
    + swallow.docs
    + ultrasonic_sensor_tester.docs
    + template.docs
)
