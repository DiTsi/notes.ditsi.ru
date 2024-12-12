# jq

## Examples

Select an element from the list that contains "entity_id"="input_boolean.home_protection" and then we take the value of the "state" key from this element

```
protectionState=$(curl -X GET -H "Authorization: Bearer ${HOMEASSISTANT_TOKEN}" -H "Content-Type: application/json" http://localhost:8123/api/states | jq -c '.[] | select(.entity_id | contains("input_boolean.home_protection"))' | jq -c '.state')
```
