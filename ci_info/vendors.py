from .env import EnvAll, EnvAny, EnvEqual, EnvExists, EnvIncludes, EnvNotEqual
from .vendor import Vendor, VendorName

# https://raw.githubusercontent.com/watson/ci-info/master/vendors.json

VENDORS: list[Vendor] = [
    Vendor(
        name=VendorName.APPVEYOR,
        env=EnvExists("APPVEYOR"),
        pr=EnvExists("APPVEYOR_PULL_REQUEST_NUMBER"),
    ),
    Vendor(
        name=VendorName.AZURE_PIPELINES,
        env=EnvExists("SYSTEM_TEAMFOUNDATIONCOLLECTIONURI"),
        pr=EnvExists("SYSTEM_PULLREQUEST_PULLREQUESTID"),
    ),
    Vendor(
        name=VendorName.APPCIRCLE,
        env=EnvExists("AC_APPCIRCLE"),
    ),
    Vendor(
        name=VendorName.BAMBOO,
        env=EnvExists("bamboo_planKey"),
    ),
    Vendor(
        name=VendorName.BITBUCKET,
        env=EnvExists("BITBUCKET_COMMIT"),
        pr=EnvExists("BITBUCKET_PR_ID"),
    ),
    Vendor(
        name=VendorName.BITRISE,
        env=EnvExists("BITRISE_IO"),
        pr=EnvExists("BITRISE_PULL_REQUEST"),
    ),
    Vendor(
        name=VendorName.BUDDY,
        env=EnvExists("BUDDY_WORKSPACE_ID"),
        pr=EnvExists("BUDDY_EXECUTION_PULL_REQUEST_ID"),
    ),
    Vendor(
        name=VendorName.BUILDKITE,
        env=EnvExists("BUILDKITE"),
        pr=EnvNotEqual("BUILDKITE_PULL_REQUEST", "false"),
    ),
    Vendor(
        name=VendorName.CIRCLE,
        env=EnvExists("CIRCLECI"),
        pr=EnvExists("CIRCLE_PULL_REQUEST"),
    ),
    Vendor(
        name=VendorName.CIRRUS,
        env=EnvExists("CIRRUS_CI"),
        pr=EnvExists("CIRRUS_PR"),
    ),
    Vendor(
        name=VendorName.CODEMAGIC,
        env=EnvExists("CM_BUILD_ID"),
        pr=EnvExists("CM_PULL_REQUEST"),
    ),
    Vendor(
        name=VendorName.CODEBUILD,
        env=EnvExists("CODEBUILD_BUILD_ARN"),
    ),
    Vendor(
        name=VendorName.CODEFRESH,
        env=EnvExists("CF_BUILD_ID"),
        pr=EnvAny(
            EnvExists("CF_PULL_REQUEST_NUMBER"),
            EnvExists("CF_PULL_REQUEST_ID"),
        ),
    ),
    Vendor(
        name=VendorName.CODESHIP,
        env=EnvAll(
            EnvEqual("CI_NAME", "codeship"),
        ),
    ),
    Vendor(
        name=VendorName.DRONE,
        env=EnvExists("DRONE"),
        pr=EnvAll(
            EnvEqual("DRONE_BUILD_EVENT", "pull_request"),
        ),
    ),
    Vendor(
        name=VendorName.WOODPECKER,
        env=EnvAll(
            EnvEqual("CI", "woodpecker"),
        ),
        pr=EnvAll(
            EnvEqual("CI_BUILD_EVENT", "pull_request"),
        ),
    ),
    Vendor(
        name=VendorName.DSARI,
        env=EnvExists("DSARI"),
    ),
    Vendor(
        name=VendorName.EAS,
        env=EnvExists("EAS_BUILD"),
    ),
    Vendor(
        name=VendorName.GITHUB_ACTIONS,
        env=EnvExists("GITHUB_ACTIONS"),
        pr=EnvAll(
            EnvEqual("GITHUB_EVENT_NAME", "pull_request"),
        ),
    ),
    Vendor(
        name=VendorName.GITLAB,
        env=EnvExists("GITLAB_CI"),
        pr=EnvExists("CI_MERGE_REQUEST_ID"),
    ),
    Vendor(
        name=VendorName.GOCD,
        env=EnvExists("GO_PIPELINE_LABEL"),
    ),
    Vendor(
        name=VendorName.LAYERCI,
        env=EnvExists("LAYERCI"),
        pr=EnvExists("LAYERCI_PULL_REQUEST"),
    ),
    Vendor(
        name=VendorName.HUDSON,
        env=EnvExists("HUDSON_URL"),
    ),
    Vendor(
        name=VendorName.JENKINS,
        env=EnvAll(
            EnvExists("JENKINS_URL"),
            EnvExists("BUILD_ID"),
        ),
        pr=EnvAny(
            EnvExists("ghprbPullId"),
            EnvExists("CHANGE_ID"),
        ),
    ),
    Vendor(
        name=VendorName.MAGNUM,
        env=EnvExists("MAGNUM"),
    ),
    Vendor(
        name=VendorName.NETLIFY,
        env=EnvExists("NETLIFY"),
        pr=EnvNotEqual("PULL_REQUEST", "false"),
    ),
    Vendor(
        name=VendorName.NEVERCODE,
        env=EnvExists("NEVERCODE"),
        pr=EnvNotEqual("NEVERCODE_PULL_REQUEST", "false"),
    ),
    Vendor(
        name=VendorName.RENDER,
        env=EnvExists("RENDER"),
        pr=EnvAll(
            EnvEqual("IS_PULL_REQUEST", "true"),
        ),
    ),
    Vendor(
        name=VendorName.SAIL,
        env=EnvExists("SAILCI"),
        pr=EnvExists("SAIL_PULL_REQUEST_NUMBER"),
    ),
    Vendor(
        name=VendorName.SEMAPHORE,
        env=EnvExists("SEMAPHORE"),
        pr=EnvExists("PULL_REQUEST_NUMBER"),
    ),
    Vendor(
        name=VendorName.SCREWDRIVER,
        env=EnvExists("SCREWDRIVER"),
        pr=EnvNotEqual("SD_PULL_REQUEST", "false"),
    ),
    Vendor(
        name=VendorName.SHIPPABLE,
        env=EnvExists("SHIPPABLE"),
        pr=EnvAll(
            EnvEqual("IS_PULL_REQUEST", "true"),
        ),
    ),
    Vendor(
        name=VendorName.SOLANO,
        env=EnvExists("TDDIUM"),
        pr=EnvExists("TDDIUM_PR_ID"),
    ),
    Vendor(
        name=VendorName.STRIDER,
        env=EnvExists("STRIDER"),
    ),
    Vendor(
        name=VendorName.TASKCLUSTER,
        env=EnvAll(
            EnvExists("TASK_ID"),
            EnvExists("RUN_ID"),
        ),
    ),
    Vendor(
        name=VendorName.TEAMCITY,
        env=EnvExists("TEAMCITY_VERSION"),
    ),
    Vendor(
        name=VendorName.TRAVIS,
        env=EnvExists("TRAVIS"),
        pr=EnvNotEqual("TRAVIS_PULL_REQUEST", "false"),
    ),
    Vendor(
        name=VendorName.VERCEL,
        env=EnvAny(
            EnvExists("NOW_BUILDER"),
            EnvExists("VERCEL_URL"),
        ),
    ),
    Vendor(
        name=VendorName.APPCENTER,
        env=EnvExists("APPCENTER_BUILD_ID"),
    ),
    Vendor(
        name=VendorName.XCODE_CLOUD,
        env=EnvExists("CI_XCODE_PROJECT"),
        pr=EnvExists("CI_PULL_REQUEST_NUMBER"),
    ),
    Vendor(
        name=VendorName.XCODE_SERVER,
        env=EnvExists("XCS"),
    ),
    Vendor(
        name=VendorName.HEROKU,
        env=EnvIncludes("NODE", "/app/.heroku/node/bin/node"),
    ),
    Vendor(
        name=VendorName.GOOGLE_CLOUD_BUILD,
        env=EnvExists("BUILDER_OUTPUT"),
    ),
    Vendor(
        name=VendorName.GERRIT,
        env=EnvExists("GERRIT_PROJECT"),
    ),
    Vendor(
        name=VendorName.RELEASEHUB,
        env=EnvExists("RELEASE_BUILD_ID"),
    ),
    Vendor(
        name=VendorName.SOURCEHUT,
        env=EnvEqual("CI_NAME", "sourcehut"),
    ),
]
