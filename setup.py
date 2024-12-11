from setuptools import find_packages,setup

setup(
    name='mcqgen',
    version='0.0.1',
    author='Mukeshwar nath',
    author_email='mukeshwarnath.cse@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)