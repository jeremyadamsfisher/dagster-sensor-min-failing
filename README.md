Adapted from https://docs.dagster.io/examples/deploy_docker.

Minimial failing example of sensor in docker-compose environment:

Run: `docker-compose up`

```
docker_example_daemon        | 2021-04-03 19:36:56 - SensorDaemon - INFO - Checking for new runs for sensor: always_skips
docker_example_daemon        | 2021-04-03 19:36:56 - SensorDaemon - ERROR - Error launching sensor run: json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
docker_example_daemon        | 
docker_example_daemon        | Stack Trace:
docker_example_daemon        |   File "/usr/local/lib/python3.7/site-packages/dagster/daemon/sensor.py", line 230, in execute_sensor_iteration
docker_example_daemon        |     sensor_debug_crash_flags,
docker_example_daemon        |   File "/usr/local/lib/python3.7/site-packages/dagster/daemon/sensor.py", line 264, in _evaluate_sensor
docker_example_daemon        |     job_state.job_specific_data.last_run_key if job_state.job_specific_data else None,
docker_example_daemon        |   File "/usr/local/lib/python3.7/site-packages/dagster/core/host_representation/repository_location.py", line 448, in get_external_sensor_execution_data
docker_example_daemon        |     last_run_key,
docker_example_daemon        |   File "/usr/local/lib/python3.7/site-packages/dagster/api/snapshot_sensor.py", line 41, in sync_get_external_sensor_execution_data_grpc
docker_example_daemon        |     last_run_key=last_run_key,
docker_example_daemon        |   File "/usr/local/lib/python3.7/site-packages/dagster/grpc/client.py", line 291, in external_sensor_execution
docker_example_daemon        |     res.serialized_external_sensor_execution_data_or_external_sensor_execution_error
docker_example_daemon        |   File "/usr/local/lib/python3.7/site-packages/dagster/serdes/serdes.py", line 236, in deserialize_json_to_dagster_namedtuple
docker_example_daemon        |     check.str_param(json_str, "json_str"), whitelist_map=_WHITELIST_MAP
docker_example_daemon        |   File "/usr/local/lib/python3.7/site-packages/dagster/serdes/serdes.py", line 246, in _deserialize_json_to_dagster_namedtuple
docker_example_daemon        |     return _unpack_value(seven.json.loads(json_str), whitelist_map=whitelist_map)
docker_example_daemon        |   File "/usr/local/lib/python3.7/json/__init__.py", line 361, in loads
docker_example_daemon        |     return cls(**kw).decode(s)
docker_example_daemon        |   File "/usr/local/lib/python3.7/json/decoder.py", line 337, in decode
docker_example_daemon        |     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
docker_example_daemon        |   File "/usr/local/lib/python3.7/json/decoder.py", line 355, in raw_decode
docker_example_daemon        |     raise JSONDecodeError("Expecting value", s, err.value) from None
```