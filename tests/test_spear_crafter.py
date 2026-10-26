#!/usr/bin/env python3
"""
PEER'S Spear Phish Crafter - Automated Unit Test Suite
Day 06: Spear Phishing Email Craft & Defense (Sqrock IT Solution)
Author: Md Peer Siddiqui
"""

import os
import sys
import json
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import spear_crafter


class TestSpearPhishCrafter(unittest.TestCase):

    def setUp(self):
        self.default_target = dict(spear_crafter.DEFAULT_TARGET)
        self.custom_target = {
            "name": "Riya Sharma",
            "email": "riya.sharma@sqrock.com",
            "company": "Sqrock",
            "domain": "sqrock.com",
            "department": "Engineering",
            "location": "Bangalore, India",
            "manager_name": "Karan Singhania",
            "role": "Frontend Developer",
            "deadline_hours": 12
        }

    def test_scenarios_data_count_and_keys(self):
        """Verify exactly 3 awareness scenarios exist with required schema fields."""
        self.assertEqual(len(spear_crafter.SCENARIOS_DATA), 3)
        for sc in spear_crafter.SCENARIOS_DATA:
            self.assertIn("id", sc)
            self.assertIn("title", sc)
            self.assertIn("category", sc)
            self.assertIn("sender_display", sc)
            self.assertIn("spoofed_from", sc)
            self.assertIn("reply_to", sc)
            self.assertIn("return_path", sc)
            self.assertIn("subject", sc)
            self.assertIn("body_template", sc)
            self.assertIn("red_flags", sc)
            self.assertTrue(len(sc["red_flags"]) >= 3)

    def test_render_scenario_body_token_replacement(self):
        """Ensure all template placeholders are cleanly replaced with target values."""
        for sc in spear_crafter.SCENARIOS_DATA:
            rendered = spear_crafter.render_scenario_body(sc, self.default_target)
            self.assertIn(self.default_target["name"], rendered["body"])
            self.assertIn(self.default_target["company"], rendered["body"])
            self.assertNotIn("{name}", rendered["body"])
            self.assertNotIn("{company}", rendered["body"])
            self.assertNotIn("{domain_spoofed}", rendered["body"])

    def test_render_mime_headers(self):
        """Verify that RFC 5322 MIME headers are generated with security markers."""
        sc = spear_crafter.SCENARIOS_DATA[0]
        rendered = spear_crafter.render_scenario_body(sc, self.default_target)
        headers = spear_crafter.render_mime_headers(rendered, self.default_target)
        
        self.assertIn("Delivered-To:", headers)
        self.assertIn("Authentication-Results:", headers)
        self.assertIn("dmarc=fail", headers)
        self.assertIn("Message-ID:", headers)
        self.assertIn("From:", headers)
        self.assertIn("Reply-To:", headers)

    def test_custom_target_profile_rendering(self):
        """Verify that a custom target from the syllabus renders properly."""
        sc = spear_crafter.SCENARIOS_DATA[1]
        rendered = spear_crafter.render_scenario_body(sc, self.custom_target)
        self.assertIn("Riya Sharma", rendered["to_header"])
        self.assertIn("Riya Sharma", rendered["body"])
        self.assertIn("riya.sharma@sqrock.com", rendered["to_header"])

    def test_export_deliverable_json(self):
        """Verify that deliverable JSON exports correctly with all sections."""
        temp_out = os.path.join(spear_crafter.TEMPLATES_DIR, "test_output.json")
        spear_crafter.export_deliverable_json(self.default_target, filepath=temp_out)
        self.assertTrue(os.path.exists(temp_out))

        with open(temp_out, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("metadata", data)
        self.assertIn("target_context", data)
        self.assertIn("spear_phishing_awareness_drafts", data)
        self.assertIn("email_authentication_defense_matrix", data)
        self.assertEqual(len(data["spear_phishing_awareness_drafts"]), 3)
        self.assertEqual(data["metadata"]["intern_name"], "Md Peer Siddiqui")

        if os.path.exists(temp_out):
            os.remove(temp_out)

    def test_dmarc_defense_policy_records(self):
        """Verify standard DMARC, SPF, and DKIM configuration syntax."""
        sc = spear_crafter.SCENARIOS_DATA[0]
        rendered = spear_crafter.render_scenario_body(sc, self.default_target)
        out_path = spear_crafter.export_deliverable_json(self.default_target)
        with open(out_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        matrix = data["email_authentication_defense_matrix"]
        self.assertTrue(matrix["spf_policy"]["value"].startswith("v=spf1"))
        self.assertTrue(matrix["dkim_policy"]["value"].startswith("v=DKIM1"))
        self.assertIn("p=reject", matrix["dmarc_policy"]["enforcement_record"])


if __name__ == "__main__":
    unittest.main()
