from django.core.management.base import BaseCommand  # type: ignore
from django.contrib.auth.models import Group, Permission, User  # type: ignore
from events.models import Event
from django.contrib.contenttypes.models import ContentType  # type: ignore


class Command(BaseCommand):
    help = "Create groups (Admin, Editor, Viewer) and sample users"

    def handle(self, *args, **options):
        ct = ContentType.objects.get_for_model(Event)
        perm_add = Permission.objects.get(codename="add_event", content_type=ct)
        perm_change = Permission.objects.get(codename="change_event", content_type=ct)
        perm_delete = Permission.objects.get(codename="delete_event", content_type=ct)

        admin_group, _ = Group.objects.get_or_create(name="Admin")
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        viewer_group, _ = Group.objects.get_or_create(name="Viewer")

        admin_group.permissions.set([perm_add, perm_change, perm_delete])
        editor_group.permissions.set([perm_add, perm_change])
        viewer_group.permissions.set([])

        # sample users
        if not User.objects.filter(username="admin_user").exists():
            u = User.objects.create_user("admin_user", password="admin123")
            u.is_staff = True
            u.save()
            admin_group.user_set.add(u)
        if not User.objects.filter(username="editor_user").exists():
            u = User.objects.create_user("editor_user", password="editor123")
            u.is_staff = True
            u.save()
            editor_group.user_set.add(u)
        if not User.objects.filter(username="viewer_user").exists():
            u = User.objects.create_user("viewer_user", password="viewer123")
            u.is_staff = False
            u.save()
            viewer_group.user_set.add(u)

        self.stdout.write(self.style.SUCCESS("Groups and sample users created."))
