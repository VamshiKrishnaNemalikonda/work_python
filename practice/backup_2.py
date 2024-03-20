#https://github.com/stackhpc/pyhelm3
#ISSUE: AttributeError: module 'typing' has no attribute 'Annotated'

import asyncio

async def process_helm_charts():
    print("Processing Helm charts")
    
    # This will use the Kubernetes configuration from the environment
    client = Client()
    # Specify the kubeconfig file to use
    client = Client(kubeconfig = "/home/fnclab/.kube/config")
    # Specify a custom Helm executable (by default, we expect 'helm' to be on the PATH)
    client = Client(executable = "/usr/local/bin/helm")


    # List the deployed releases
    releases = await client.list_releases(all = True, all_namespaces = True)
    for release in releases:
        revision = await release.current_revision()
        print(release.name, release.namespace, revision.revision, str(revision.status))

    # Get the current revision for an existing release
    revision = await client.get_current_revision("cert-manager", namespace = "cert-manager")
    chart_metadata = await revision.chart_metadata()
    print(
        revision.release.name,
        revision.release.namespace,
        revision.revision,
        str(revision.status),
        chart_metadata.name,
        chart_metadata.version
    )

    # Fetch a chart
    chart = await client.get_chart(
        "cert-manager",
        repo = "https://charts.jetstack.io",
        #version = "v1.8.x"
        version = "1.14.4"
    )
    print(chart.metadata.name, chart.metadata.version)
    print(await chart.readme())

    # Install or upgrade a release
    revision = await client.install_or_upgrade_release(
        "cert-manager",
        chart,
        { "installCRDs": True },
        atomic = True,
        wait = True
    )
    print(
        revision.release.name,
        revision.release.namespace,
        revision.revision,
        str(revision.status)
    )

    # Uninstall a release
    #   Via the revision
    #revision = await client.get_current_revision("cert-manager", namespace = "cert-manager")
    #await revision.release.uninstall(wait = True)
    #   Or directly by name
    #await client.uninstall_release("cert-manager", namespace = "cert-manager", wait = True)