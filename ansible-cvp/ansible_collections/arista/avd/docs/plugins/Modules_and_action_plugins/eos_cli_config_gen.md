---
# This title is used for search results
title: arista.avd.eos_cli_config_gen
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_cli_config_gen

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_cli_config_gen` when using this plugin.

Generate AVD EOS device configurations and documentations

## Synopsis

The `arista.avd.eos_cli_config_gen` module is an Ansible Action Plugin providing the following capabilities:

- Validates input variables according to eos_cli_config_gen schema
- Generates device configuration and saves it to file
- Optionallu generates device documentation and saves it to file

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>structured_config_filename</samp> | str | optional | None |  | The path of the structured config to load. Required if read_structured_config_from_file is true. |
| <samp>config_filename</samp> | str | optional | None |  | The path to save the generated config to. Required if generate_device_config is true. |
| <samp>documentation_filename</samp> | str | optional | None |  | The path to save the generated documentation. Required if generate_device_doc is true. |
| <samp>read_structured_config_from_file</samp> | bool | optional | True |  | Flag to indicate if the structured config should be read from a file or not. |
| <samp>generate_device_config</samp> | bool | optional | True |  | Flag to generate the device configuration. |
| <samp>generate_device_doc</samp> | bool | optional | True |  | Flag to generate the device documentation. |
| <samp>device_doc_toc</samp> | bool | optional | True |  | Flag to generate the table of content for the device documentation. |
| <samp>conversion_mode</samp> | str | False | debug | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>quiet</code><br>- <code>disabled</code> | Run data conversion in either &#34;error&#34;, &#34;warning&#34;, &#34;info&#34;, &#34;debug&#34;, &#34;quiet&#34; or &#34;disabled&#34; mode.<br>Conversion will perform type conversion of input variables as defined in the schema.<br>Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.<br>During conversion, messages will be generated with information about the host(s) and key(s) which required conversion.<br>conversion_mode:disabled means that conversion will not run.<br>conversion_mode:error will produce error messages and fail the task.<br>conversion_mode:warning will produce warning messages.<br>conversion_mode:info will produce regular log messages.<br>conversion_mode:debug will produce hidden messages viewable with -v.<br>conversion_mode:quiet will not produce any messages. |
| <samp>validation_mode</samp> | str | False | warning | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>disabled</code> | Run validation in either &#34;error&#34;, &#34;warning&#34;, &#34;info&#34;, &#34;debug&#34; or &#34;disabled&#34; mode.<br>Validation will validate the input variables according to the schema.<br>During validation, messages will be generated with information about the host(s) and key(s) which failed validation.<br>validation_mode:disabled means that validation will not run.<br>validation_mode:error will produce error messages and fail the task.<br>validation_mode:warning will produce warning messages.<br>validation_mode:info will produce regular log messages.<br>validation_mode:debug will produce hidden messages viewable with -v. |
| <samp>cprofile_file</samp> | str | False | None |  | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |

## Examples

```yaml
---
- name: Generate eos intended configuration and device documentation
  arista.avd.eos_cli_config_gen:
    structured_config_filename: "{{ structured_config_filename }}"
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    read_structured_config_from_file: true
  delegate_to: localhost
  vars:
    structured_config_filename: "{{ structured_dir }}/{{ inventory_hostname }}.{{ avd_structured_config_file_format }}"
- name: Generate device documentation only
  arista.avd.eos_cli_config_gen:
    structured_config_filename: "{{ structured_config_filename }}"
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    read_structured_config_from_file: true
    generate_device_config: false
    device_doc_toc: true
  delegate_to: localhost
  vars:
    structured_config_filename: "{{ structured_dir }}/{{ inventory_hostname }}.{{ avd_structured_config_file_format }}"
```

## Authors

- Arista Ansible Team (@aristanetworks)
