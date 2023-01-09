import boto3



def get_resource_s3(region_name: str) -> None:

    boto3.resource("s3", region_name=region_name)


def main() -> None:

    get_resource_s3("ap-southeast-1")


if __name__ == "__main__":

    main()
