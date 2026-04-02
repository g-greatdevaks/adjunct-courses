# Adjunct Faculty Course Materials - By greatdevaks

This repository contains academic course materials for various courses instructed by Anmol Krishan Sachdeva (greatdevaks) in the capacity of Adjunct Faculty at multiple institutions and universities.

## Repository Relevance

The primary objective of this repository is to archive and share pedagogical resources, including lecture notes, workshop modules, and laboratory exercises. The materials are intended for educational reference and dissemination.

## Academic and Professional Profile

Anmol Krishan Sachdeva (greatdevaks) is a seasoned technologist who has spoken at 100+ global conferences, bridging technical deep dives with architectural strategies. He helps organizations navigate emerging technologies for driving key business outcomes.

An advocate for sustainable innovation, he currently serves as a Sr. Solutions Engineer (Platform Engineering) at Google. Balancing industry with academia, Anmol is a Distinguished Lecturer, an Adjunct Professor, and a published researcher.

- **LinkedIn**: [linkedin.com/in/greatdevaks](https://www.linkedin.com/in/greatdevaks)
- **Twitter**: [twitter.com/greatdevaks](https://www.twitter.com/greatdevaks)
- **Sessionize**: [sessionize.com/greatdevaks](https://sessionize.com/greatdevaks)

## Course Catalog

The course materials are organized by institution or subject area.

_(The course listing is to be populated as the repository develops.)_

## Repository Structure

The repository contains several configuration files to maintain code quality and consistency:

- **`.editorconfig`** (https://editorconfig.org): Defines and maintains consistent coding styles between different editors and IDEs.
- **`.gitignore`** (https://git-scm.com/docs/gitignore): Specifies intentionally untracked files that Git should ignore.
- **`.pre-commit-config.yaml`** (https://pre-commit.com): Configuration for `pre-commit` hooks (Linters, Formatters, Security Scoring, etc.).

## Local Development

The preservation of code quality is facilitated through the utilization of `pre-commit` hooks for Python, SQL, and standard file formats.

### Installation Methodologies

Installation procedures are contingent upon the host operating system.

#### macOS

The Homebrew package manager can be utilized for installation:

```bash
# https://brew.sh
brew install pre-commit
```

#### Linux

The Python package installer (`pip`) or `pipx` can be utilized for installation:

```bash
# https://pip.pypa.io/en/stable/
pip install pre-commit

# https://pypa.github.io/pipx/ (Preferred for isolation)
pipx install pre-commit
```

#### Windows

The Python package installer or the Chocolatey package manager can be utilized for installation:

```bash
# https://pip.pypa.io/en/stable/
pip install pre-commit

# https://chocolatey.org
choco install pre-commit
```

### Fallback Installation (Absence of Package Managers)

In scenarios where package managers are unavailable, the installation of the Python runtime environment remains the primary prerequisite, as it facilitates the retrieval of parameters via standard package acquisition channels. Alternatively, direct retrieval of pre-compiled binaries from official release repositories may be pursued.

### Hook Suite Initialization

Subsequent to installation, navigation to the repository root and initialization of the Git hooks can be performed via:

```bash
pre-commit install
```

Automated verification checks are executed upon each invocation of the `git commit` command.

### Manual Verification

Forced execution of verification checks across the entirety of the codebase can be achieved via:

```bash
pre-commit run --all-files
```

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This repository and its course materials are licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## Disclaimer

The work and thoughts presented in the repository represent the author's own learnings and are inspired by their experiences. The work does not reflect views, opinions, or thoughts, nor is it endorsed by, the author's employer or any professional bodies or organizations they are associated with.
