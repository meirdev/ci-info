import enum
from typing import NamedTuple

from .env import Env, EnvList


class VendorName(str, enum.Enum):
    APPVEYOR = "AppVeyor"
    AZURE_PIPELINES = "Azure Pipelines"
    APPCIRCLE = "Appcircle"
    BAMBOO = "Bamboo"
    BITBUCKET = "Bitbucket Pipelines"
    BITRISE = "Bitrise"
    BUDDY = "Buddy"
    BUILDKITE = "Buildkite"
    CIRCLE = "CircleCI"
    CIRRUS = "Cirrus CI"
    CODEMAGIC = "Codemagic"
    CODEBUILD = "AWS CodeBuild"
    CODEFRESH = "Codefresh"
    CODESHIP = "Codeship"
    DRONE = "Drone"
    WOODPECKER = "Woodpecker"
    DSARI = "dsari"
    EAS = "Expo Application Services"
    GITHUB_ACTIONS = "GitHub Actions"
    GITLAB = "GitLab CI"
    GOCD = "GoCD"
    LAYERCI = "LayerCI"
    HUDSON = "Hudson"
    JENKINS = "Jenkins"
    MAGNUM = "Magnum CI"
    NETLIFY = "Netlify CI"
    NEVERCODE = "Nevercode"
    RENDER = "Render"
    SAIL = "Sail CI"
    SEMAPHORE = "Semaphore"
    SCREWDRIVER = "Screwdriver"
    SHIPPABLE = "Shippable"
    SOLANO = "Solano CI"
    STRIDER = "Strider CD"
    TASKCLUSTER = "TaskCluster"
    TEAMCITY = "TeamCity"
    TRAVIS = "Travis CI"
    VERCEL = "Vercel"
    APPCENTER = "Visual Studio App Center"
    XCODE_CLOUD = "Xcode Cloud"
    XCODE_SERVER = "Xcode Server"
    HEROKU = "Heroku"
    GOOGLE_CLOUD_BUILD = "Google Cloud Build"
    GERRIT = "Gerrit"
    RELEASEHUB = "ReleaseHub"
    SOURCEHUT = "Sourcehut"


class Vendor(NamedTuple):
    name: VendorName
    env: Env | EnvList
    pr: Env | EnvList | None = None
