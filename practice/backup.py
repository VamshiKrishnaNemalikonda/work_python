def process_helm_charts():
    print("Processing Helm charts")
    # Load the Helm chart
    chart = pyhelm.load_chart('./my-chart')
    # Get the chart's values
    values = chart.values

    # Get the chart's templates
    templates = chart.templates

    # Render the chart's templates
    rendered_templates = chart.render_templates(values)

    # Get the chart's manifest
    manifest = chart.manifest

    # Deploy the chart to Kubernetes
    client.CoreV1Api().create_namespaced_deployment(namespace='default', body=manifest)