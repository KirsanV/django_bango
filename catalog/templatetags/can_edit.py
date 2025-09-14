from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_owner(context, obj):
    """
    Возвращает True если текущий пользователь аутентифицирован и является владельцем объекта.
    Ожидается, что объект имеет поле owner или owner_id.
    Пример в шаблоне: {% is_owner product as product_is_owner %}
    """
    request = context.get("request")
    if not request:
        return False
    user = request.user
    if not user.is_authenticated:
        return False
    owner_id = getattr(obj, "owner_id", None)
    if owner_id is not None:
        return owner_id == user.id
    owner = getattr(obj, "owner", None)
    if owner is None:
        return False
    try:
        return getattr(owner, "id", owner) == user.id
    except Exception:
        return False

@register.simple_tag(takes_context=True)
def can_delete(context, obj, moderator_group_name="ProductModerators"):
    """
    Возвращает True если текущий пользователь — владелец объекта или состоит в группе модераторов.
    По умолчанию проверяет группу "ProductModerators", можно передать другое имя группы в шаблоне.
    Пример: {% can_delete product as product_can_delete %}
    """
    request = context.get("request")
    if not request:
        return False
    user = request.user
    if not user.is_authenticated:
        return False

    if is_owner(context, obj):
        return True
    try:
        return user.groups.filter(name=moderator_group_name).exists()
    except Exception:
        return False

@register.simple_tag(takes_context=True)
def can_edit(context, obj):
    """
    По условию задания редактировать может только владелец, поэтому тут просто проксируем is_owner.
    {% can_edit product as product_can_edit %}
    """
    return is_owner(context, obj)