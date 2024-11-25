# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.generate_lacp_id"

try:
    from pyavd.j2filters import generate_lacp_id
except ImportError as e:
    generate_lacp_id = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )

DOCUMENTATION = r"""
---
name: generate_lacp_id
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi `0303:0202:0101` to LACP ID format `0303.0202.0101`
description: Replaces `:` with `.`
positional: _input
options:
  _input:
    description: Short ESI value as per AVD definition in eos_designs.
    type: string
    required: true
deprecated:
    removed_in: "5.0.0"
    why: This filter is no longer used by AVD and is very simple to replace with a generic Jinja filter.
    alternative: Use the builtin `replace` filter instead like `{{ <short_esi> | replace(':', '.') }}`
"""

EXAMPLES = r"""
---
lacp_id: "{{ short_esi | arista.avd.generate_lacp_id }}"
"""

RETURN = r"""
---
_value:
  description: String based on LACP ID format like 0303.0202.0101
  type: string
"""


class FilterModule(object):
    def filters(self):
        return {
            "generate_lacp_id": wrap_filter(PLUGIN_NAME)(generate_lacp_id),
        }
