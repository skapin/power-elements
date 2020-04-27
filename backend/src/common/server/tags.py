
from flask_restful import Resource, reqparse
from common.db.tools import to_dict, serialize
from common.db import models
from common.server.flaskutils import abort_doesnt_exist
from server.extensions import db


class TagSearch(Resource):
    def get(self, session):
        results = models.Tag.query.join(
            models.Session).filter_by(
            uniqid=session).order_by(
            models.Tag.at).all()
        tags = []
        for s in results:
            d = serialize(to_dict(s))
            tags.append(d)
        return tags


class TagView(Resource):
    def get(self, id):
        tag = models.Tag.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(tag)

        return serialize(to_dict(tag))

    def delete(self, id):
        tag = models.Tag.query.filter_by(uniqid=id).first()
        abort_doesnt_exist(tag)
        db.tag.delete(tag)
        db.tag.commit()

        return '', 204


parser = reqparse.RequestParser()
parser.add_argument('type')
parser.add_argument('session_id')
parser.add_argument('by')
parser.add_argument('comment')


class TagListView(Resource):
    def get(self):
        tags = []
        for s in models.Tag.query.all():
            d = serialize(to_dict(s))
            tags.append(d)
        return tags

    def post(self):
        args = parser.parse_args()
        type_ = args['type']
        if type_ != "WARNING" and type_ != "HEAVY" and type_ != "STOP":
            mtm_ = True
        else:
            mtm_ = False
        comment_ = args.get('comment', '')

        tag = models.Tag(
            by=args['by'],
            type=type_,
            comment=comment_,
            session_obj=models.Session.query.filter_by(
                uniqid=args['session_id']).first(),
            mtm=mtm_)
        db.session.add(tag)
        db.session.commit()

        return serialize(to_dict(tag)), 201
