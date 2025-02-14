# Home Assistant

## Automations

```YAML
- alias: Motion on camera (nobody's home)
  initial_state: true
  trigger:
  - platform: state
    entity_id: binary_sensor.dahua_motion
    from: 'off'
    to: 'on'
  condition:
  - condition: or
    conditions:
    - condition: state
      entity_id: group.family
      state: 'not_home'
    - condition: state #!
      entity_id: input_boolean.test_button
      state: 'on'
  action:
  # - service: shell_command.light_on
  - service: notify.mobile_app_pixel_5 #!
    data:
      title: "Moving at home"
      message: TTS
      data:
        ttl: 0
        priority: high
        channel: alarm_stream
  # - service: notify.notify
  #   data:
  #     message: "Moving at home"
  #     data:
  #       actions:
  #         - action: "URI"
  #           title: "Camera"
  #           uri: "entityId:camera.dahua"
  - service: tts.google_translate_say
    data:
      entity_id: media_player.backup_server
      message: "Несанкционированное проникновение. Вы будете нейтрализованы"
      language: "ru"
  # - delay: 120
  # - service: shell_command.light_off
  - delay: 15
  mode: single
```

## Conditions

```YAML
  condition:
  - condition: or
    conditions:
    - condition: state
      entity_id: group.family
      state: 'not_home'
    - condition: state #!
      entity_id: input_boolean.test_button
      state: 'on'
      
```

## Triggers

```YAML
trigger:
- platform: state
  entity_id: binary_sensor.dahua_motion
  from: 'off'
  to: 'on'
```

## Services

```YAML
# Notification with actions
- service: notify.notify
  data:
    message: "Moving at home"
    data:
      actions:
        - action: "URI"
          title: "Camera"
          uri: "entityId:camera.dahua"
```

## service_template

```YAML
  - service_template: >
      {% for state in states.device_tracker %}
        {% if is_state(state.entity_id, 'home') %}
          {{ 'notify.mobile_app_' + state.entity_id | replace('device_tracker.', '') }}
        {% endif %}
      {% endfor %}
    data:
      message: 'Anyone comes'
```
