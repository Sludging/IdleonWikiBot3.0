from repositories.misc.world7.JellyCellRepo import JellyCellRepo
from repositories.misc.world7.JellyFeverRepo import JellyFeverRepo
from repositories.misc.world7.JellyOperationMetadataRepo import JellyOperationMetadataRepo
from repositories.misc.world7.JellyObstructionRepo import JellyObstructionRepo
from repositories.misc.world7.JellyOperatorUpgradeRepo import JellyOperatorUpgradeRepo

JellyOperatorRepos = [
    JellyOperatorUpgradeRepo,
    JellyObstructionRepo,
    JellyCellRepo,
    JellyFeverRepo,
    JellyOperationMetadataRepo,
]
