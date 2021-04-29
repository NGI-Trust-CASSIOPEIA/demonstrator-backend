# Lock sensor

## Configurations - Lock sensor

Add the following lines on configuration file: `configuration.yaml`

```
lock:
  - platform: mqtt
    name: Frontdoor
    state_topic: "home-assistant/frontdoor/"
    command_topic: "home-assistant/frontdoor/set"
    payload_lock: "LOCK"
    payload_unlock: "UNLOCK"
    state_locked: "LOCK"
    state_unlocked: "UNLOCK"
    optimistic: false
    qos: 1
    retain: true

```