from setuptools import setup, find_packages

setup(
    name='research_agent',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pydantic>=2.5.0',
        'requests>=2.31.0',
        'arxiv>=2.1.0',
        'chromadb>=0.4.22',
        'python-dotenv>=1.0.0',
        'tiktoken>=0.5.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.3',
            'black>=23.11.0',
            'flake8>=6.1.0',
        ],
    },
    python_requires='>=3.9',
)
