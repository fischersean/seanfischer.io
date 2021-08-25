from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_certificatemanager as certificates,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
)


class SeanfischerIoStack(core.Stack):
    def __init__(
        self, scope: core.Construct, construct_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        frontend_bucket = self.S3_FRONTENDDEPLOY()

    def S3_FRONTENDDEPLOY(self):
        bucket = s3.Bucket(
            self,
            "FrontendBucket",
            removal_policy=core.RemovalPolicy.DESTROY,
            versioned=True,
        )

        distribution = cloudfront.Distribution(
            self,
            "FrontendDistribution",
            # TODO: The domain and cert info should be env vars
            domain_names=["www.seanfischer.io"],
            certificate=certificates.Certificate.from_certificate_arn(
                self,
                "DomainCertificateEast1",
                "arn:aws:acm:us-east-1:261392311630:certificate/859dc9d1-7a5f-4474-bcad-bcba1607a5ed",
            ),
            default_root_object="index.html",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(
                    bucket,
                ),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
        )

        s3deploy.BucketDeployment(
            self,
            "FrontendS3Deployment",
            sources=[s3deploy.Source.asset("./src")],
            destination_bucket=bucket,
            distribution=distribution,
        )

        return bucket
