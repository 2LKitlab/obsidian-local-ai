
from setuptools import setup, find_packages
setup(
    name='obsidian-local-ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'obsidian-assistant=obsidianai.llm:execute'
        ]
    },
    python_requires='>=3.6',
)
