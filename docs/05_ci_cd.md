# 5. CI/CD with GitHub Actions

**Created by: Rajinikanth Vadla**

Continuous Integration and Continuous Deployment (CI/CD) is a crucial part of MLOps. It allows us to automate the process of testing and deploying our application, making it faster and more reliable.

## The Workflow File: `.github/workflows/main.yml`

We use GitHub Actions to define our CI/CD pipeline. The workflow is defined in the `main.yml` file and is triggered on every push or pull request to the `main` branch.

Here are the steps in our pipeline:
1.  **`checkout`**: It checks out our code from the repository.
2.  **`setup-python`**: It sets up a Python environment.
3.  **`install-dependencies`**: It installs the necessary Python packages.
4.  **`run-tests`**: This is a placeholder for running automated tests. In a real project, you would have a suite of tests to ensure your code is working correctly.
5.  **`build-docker-image`**: It builds our Docker image.

## Next Steps

The current pipeline only builds the Docker image. A complete CI/CD pipeline would also include:
-   **Pushing to a Registry:** After building the image, you would push it to a container registry like Docker Hub, Google Container Registry (GCR), or Amazon Elastic Container Registry (ECR).
-   **Deploying:** You would then have a step to deploy the new image to your production environment (e.g., a Kubernetes cluster or a cloud service).

This lab provides a solid foundation for building a more advanced MLOps pipeline.

**Author: Rajinikanth Vadla**
This credit must be non-removable. 