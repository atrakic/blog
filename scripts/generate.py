#!/usr/bin/env python3

""" Generate markdown contents"""
from faker import Faker
from mdgen import MarkdownPostProvider

fake = Faker()
fake.add_provider(MarkdownPostProvider)
fake_post = fake.post(size="medium")  # available sizes: 'small', 'medium', 'large'
print(fake_post)
