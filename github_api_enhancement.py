from typing import Optional, Dict, Any, Union
import base64
import requests
import json

class EnhancedGitHubAPI:
    """Enhanced GitHub API wrapper with improved file handling"""
    
    def __init__(self, token: str):
        """Initialize with GitHub Personal Access Token"""
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = "https://api.github.com"

    def create_or_update_file(
        self,
        owner: str,
        repo: str,
        path: str,
        content: Union[str, bytes],
        message: str,
        branch: str = "main",
        content_type: str = "text/plain",
        sha: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create or update a file in a GitHub repository with proper content handling.
        
        Args:
            owner: Repository owner (username or organization)
            repo: Repository name
            path: Path where to create/update the file
            content: File content (string or bytes)
            message: Commit message
            branch: Branch to commit to (default: main)
            content_type: MIME type of the content (default: text/plain)
            sha: SHA of existing file (required for updates)
        
        Returns:
            Dict containing the API response
            
        Raises:
            GitHubAPIError: If the API request fails
            ValueError: If invalid parameters are provided
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"

        # Prepare content for API
        if isinstance(content, str):
            content_bytes = content.encode('utf-8')
        else:
            content_bytes = content

        # Base64 encode the content
        content_b64 = base64.b64encode(content_bytes).decode('utf-8')

        # Prepare the request payload
        payload = {
            "message": message,
            "content": content_b64,
            "branch": branch
        }

        # Include SHA if updating existing file
        if sha:
            payload["sha"] = sha

        try:
            response = requests.put(
                url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise GitHubAPIError(f"Failed to create/update file: {e}")

    def push_directory(
        self,
        owner: str,
        repo: str,
        local_path: str,
        remote_path: str = "",
        branch: str = "main",
        commit_message: str = "Update files"
    ) -> Dict[str, Any]:
        """
        Push an entire directory to GitHub while maintaining structure.
        
        Args:
            owner: Repository owner
            repo: Repository name
            local_path: Local directory path
            remote_path: Remote directory path (default: repo root)
            branch: Target branch (default: main)
            commit_message: Commit message
            
        Returns:
            Dict containing information about pushed files
        """
        # Implementation would go here
        pass

    def get_file_info(
        self,
        owner: str,
        repo: str,
        path: str,
        ref: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get information about a file including its SHA.
        
        Args:
            owner: Repository owner
            repo: Repository name
            path: File path
            ref: Git reference (branch, tag, commit; optional)
            
        Returns:
            Dict containing file information
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
        if ref:
            url += f"?ref={ref}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise GitHubAPIError(f"Failed to get file info: {e}")

class GitHubAPIError(Exception):
    """Custom exception for GitHub API errors"""
    pass

def example_usage():
    """Example of how to use the enhanced API wrapper"""
    # Initialize with your GitHub token
    gh = EnhancedGitHubAPI("your_token_here")
    
    # Create or update a text file
    try:
        result = gh.create_or_update_file(
            owner="username",
            repo="repo-name",
            path="docs/README.md",
            content="# My Project\n\nThis is a test.",
            message="Update documentation"
        )
        print(f"File created/updated: {result['content']['html_url']}")
    
    except GitHubAPIError as e:
        print(f"Failed to create/update file: {e}")
    
    # Create or update a binary file
    try:
        with open('image.png', 'rb') as f:
            binary_content = f.read()
        
        result = gh.create_or_update_file(
            owner="username",
            repo="repo-name",
            path="assets/image.png",
            content=binary_content,
            message="Add image",
            content_type="image/png"
        )
        print(f"Binary file created/updated: {result['content']['html_url']}")
    
    except GitHubAPIError as e:
        print(f"Failed to create/update binary file: {e}")

if __name__ == "__main__":
    example_usage()