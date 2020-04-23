from flask_restful import Resource


class ProjectRepo(Resource):
    def get(self):
        from project_repo.model import Project
        all_project = Project.query.all()
        return Project.schemas.dump(all_project)
