# Google BigQuery

## Sequence

```
#standardSQL
SELECT
...,
...
FROM
...
WHERE
...
GROUP BY
...
ORDER BY
...
```

## Examples

```SQL
-- CONCATENATE STRINGS
SELECT
CONCAT(time_in, ' - ', time_out) as time_inout
FROM ...


-- CASE
SELECT
CASE event_id
WHEN 4800 THEN 'lock'
WHEN 4801 THEN 'unlock'
WHEN 4647 THEN 'logoff'
WHEN 4648 THEN 'logon'
END AS event,
...
FROM
...
--
CASE
WHEN starting_time IS NULL THEN "-"
ELSE starting_time
END AS starting_time


-- ORDER BY
ORDER BY
timestamp DESC,
username


-- JOIN
SELECT
early_events.date,
early_events.time,
early_events.user,
all_events.timestamp
FROM (
SELECT
date,
MIN(time) AS time,
user
FROM
`base1`) AS early_events
JOIN (
SELECT
time,
user,
date
FROM
`base2` ) AS all_events
ON
(early_events.time = all_events.time
AND early_events.date = all_events.date)


-- UNION
#standardSQL
SELECT
*
FROM
`dt1`
UNION ALL
SELECT
*
FROM
`dt2`


-- PARTITION BY
SELECT
*
FROM (
SELECT
email,
date,
ROW_NUMBER() OVER (PARTITION BY email ORDER BY date DESC) AS seqnum
FROM
`dt1` )
WHERE
seqnum <= 7
```

## Functions

```
LOWER(username)
REGEXP_CONTAINS(username, r"^[a-z]+\.[a-z]+$")
date(timestamp) as date
time(timestamp, "Europe/Moscow") as time
MIN(time) AS time
MAX(time) AS time
CAST(time_in AS STRING)
REGEXP_REPLACE(
CAST(TIME(TIMESTAMP_MICROS(TIME_DIFF(time_out, time_in, MICROSECOND))) AS STRING),
r"([0-9]{1,2}):([0-9]{1,2}):([0-9]{1,2}).[0-9]+", r"\1:\2"
)
CURRENT_DATE()
COUNTIF(field NOT LIKE "-") AS qwerty
AVG(work_micros)
```

## Conditions

```SQL
WHERE
mes LIKE "hello"
AND ((message IS NULL)
OR (message NOT LIKE "%HELLO%"
AND message NOT LIKE "%HELL*WORLD%"))
```