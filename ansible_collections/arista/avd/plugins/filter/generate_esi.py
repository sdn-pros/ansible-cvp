# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.generate_esi"

try:
    from pyavd.j2filters import generate_esi
except ImportError as e:
    generate_esi = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )


DOCUMENTATION = r"""
---
name: generate_esi
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1"
short_description: Transforms short_esi `0303:0202:0101` to EVPN ESI format `0000:0000:0303:0202:0101`
description: Concatenates the given `esi_prefix` and `short_esi`.
positional: _input
options:
  _input:
    description: Short ESI value as per AVD definition in eos_designs.
    type: string
    required: true
  esi_prefix:
    description: ESI prefix value. Will be concatenated with the `short_esi`.
    type: string
    default: "0000:0000:"
deprecated:
    removed_in: "5.0.0"
    why: This filter is no longer used by AVD and is very simple to replace with generic Jinja syntax.
    alternative: Use Jinja string concatenation instead like `{{ <esi_prefix> ~ <short_esi> }}`
"""

EXAMPLES = r"""
---
esi: "{{ short_esi | arista.avd.generate_esi('deaf:beed:') }}"
"""

RETURN = r"""
---
_value:
  description: Concatenated string of `esi_prefix` and `short_esi` like `0000:0000:0303:0202:0101`
  type: string
"""


class FilterModule(object):
    def filters(self):
        return {
            "generate_esi": wrap_filter(PLUGIN_NAME)(generate_esi),
        }
