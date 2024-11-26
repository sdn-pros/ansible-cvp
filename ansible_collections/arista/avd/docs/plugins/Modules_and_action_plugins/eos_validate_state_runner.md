---
# This title is used for search results
title: arista.avd.eos_validate_state_runner
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_validate_state_runner

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_validate_state_runner` when using this plugin.

Uses ANTA for eos_validate_state role

## Synopsis

The `arista.avd.eos_validate_state_runner` module is an Ansible Action Plugin leveraging the ANTA test framework to validate that the generated structured configurations by AVD are applied to the devices and that the deployed network is working correctly.

This plugin requires a valid structured configuration for each device in the hostvars; otherwise, some tests will not be generated.

The plugin offers the following capabilities:
    - Generating a per-device test catalog based on the AVD structured_config.
    - Running generated tests against each device, saving the results in a single JSON file per-device.
    - In check_mode, only the test catalog is generated, and a report is created to preview the tests that would be run against each device.
    - Saving per-device test catalogs and results in specified directories for use by the `eos_validate_state_reports` plugin.
    - Maintaining backward compatibility with existing ansible tags for eos_validate_state to filter test categories.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>logging_level</samp> | str | optional | WARNING | Valid values:<br>- <code>CRITICAL</code><br>- <code>ERROR</code><br>- <code>WARNING</code><br>- <code>INFO</code><br>- <code>DEBUG</code> | Sets the log level for the ANTA library. Defaults to &#34;WARNING&#34; if not specified. |
| <samp>save_catalog</samp> | bool | optional | False |  | Indicates whether to save the test catalog for each device. |
| <samp>device_catalog_path</samp> | str | optional | None |  | The absolute path where the device test catalog will be saved.<br>Required if `save_catalog` is set to `True`. |
| <samp>test_results_dir</samp> | str | optional | None |  | The directory where the test results JSON file for each host will be saved. |
| <samp>custom_anta_catalogs_dir</samp> | any | optional | None |  | The directory where custom ANTA test catalogs are stored.<br>Files must be named after the device hostname or the Ansible group name and have a `.yml` or `.yaml` extension. |
| <samp>skip_tests</samp> | list | optional | None |  | A list of dictionaries specifying categories and, optionally, tests to skip.<br>Each dictionary must have a key `category` and can optionally include a `tests` key. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;category</samp> | str | optional | None |  | The name of an AvdTest category (e.g., `AvdTestHardware`). |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;tests</samp> | list | optional | None |  | An optional list of specific tests in the category to skip (e.g., `VerifyRoutingProtocolModel` in `AvdTestBGP`).<br>If not specified, all tests in the category are considered.<br>For a complete list of available tests, see [link to the test list](https://avd.arista.com/stable/roles/eos_validate_state/anta_integration.html#test-categories). |
| <samp>cprofile_file</samp> | any | optional | None |  | The filename for storing cProfile data, useful for debugging performance issues.<br>Be aware that enabling cProfile can affect performance, so use it only for troubleshooting. |

## Notes

- Enabling the cProfile feature for performance profiling may impact the plugin&#39;s performance, especially in production environments.
- The plugin manages the creation of JSON files, which are used for storing test results. For each device, one JSON file containing all results is saved in the test results directory.
- The file naming convention is hard coded as &#34;&lt;inventory_hostname&gt;-results.json&#34; and cannot be changed. This ensures that the report plugin can properly retrieve the files.
- This module supports `check_mode`, allowing the generation of test reports without executing the tests.
- Regardless of whether they are running in `check_mode` or not, the reports are generated by the `eos_validate_state_reports` plugin.

## See Also

- ANTA website: [https://anta.arista.com](https://anta.arista.com)<br>Documentation for the ANTA test framework

## Examples

```yaml
- name: Execute eos_validate_state_runner leveraging ANTA
  arista.avd.eos_validate_state_runner:
    logging_level: ERROR
    save_catalog: true
    device_catalog_path: "/my_avd_project/intended/test_catalogs/{{ inventory_hostname }}-catalog.yml"
    test_results_dir: "/my_avd_project/reports/test_results"
    custom_anta_catalogs_dir: "/my_avd_project/custom_anta_catalogs"
    skip_tests:
      - category: AvdTestHardware
      - category: AvdTestBGP
        tests:
          - VerifyRoutingProtocolModel
  register: anta_results
```

## Authors

- Arista Ansible Team (@aristanetworks)