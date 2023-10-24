from django.shortcuts import render

# Create your views here.


def showarticle(request):
    title = 'My article'
    author = 'Njongo'
    article_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sed aliquam justo, sollicitudin pharetra mauris. Sed non purus non magna semper tristique eu vel arcu. Nullam mattis, turpis ac luctus porta, erat lacus tincidunt nibh, suscipit scelerisque felis diam eget libero. Sed euismod, ex vel eleifend lobortis, augue metus lobortis dolor, sit amet egestas mi metus vel est. Morbi vitae scelerisque turpis. Praesent in purus vel erat aliquet porta nec non ante. Suspendisse viverra elit ut congue varius. Vivamus aliquam ligula vitae ornare egestas. Nullam fermentum volutpat gravida. Duis a magna enim. Nunc sit amet tellus sed risus auctor sollicitudin. Nulla fermentum porttitor velit, quis cursus nibh.

Curabitur non turpis eu orci iaculis aliquet quis vitae turpis. Pellentesque maximus purus magna, at feugiat risus aliquam et. Nam iaculis nec dui et dignissim. Donec quis nunc posuere, vestibulum eros non, tempus nunc. Nam dui libero, consequat eget sem ut, congue convallis orci. Nulla scelerisque massa ligula, consequat interdum enim fermentum nec. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis ut quam libero. Donec et venenatis arcu, eu pretium enim. Nullam aliquam, erat et dapibus scelerisque, erat sapien feugiat tortor, at faucibus mauris tellus non ligula. Nam cursus quam ut hendrerit porta. Morbi sed lorem placerat, pharetra arcu sit amet, tincidunt massa. Maecenas accumsan posuere tellus sit amet vehicula. Fusce vehicula lacus sit amet suscipit posuere. Quisque vel auctor ante, et imperdiet mi. Integer eu ornare est.

Duis ac dapibus nisl, et gravida ex. In hac habitasse platea dictumst. Mauris porttitor congue dui et efficitur. In et enim tellus. Duis scelerisque orci nec enim lacinia consequat. Fusce venenatis, velit nec rhoncus mollis, nulla nunc euismod massa, vel feugiat nunc augue vitae magna. Proin feugiat ligula ac laoreet vehicula. Sed molestie ac dui a fermentum. Sed sit amet laoreet urna. Vestibulum mattis ante nec cursus congue. Quisque rhoncus nibh nec quam accumsan finibus. Sed eu hendrerit sem, in aliquam leo. Vivamus dictum tempor turpis aliquet auctor. Phasellus pretium ultricies cursus. Ut venenatis at enim vitae varius.

Donec euismod dignissim accumsan. Etiam euismod varius nunc posuere blandit. Nunc et congue magna, ac ultricies nisl. Aliquam erat volutpat. Integer ac tellus mauris. Praesent dictum, nisl ut rutrum cursus, lacus velit tempor ante, quis interdum nunc sem a ligula. Phasellus lobortis libero ac imperdiet venenatis. Sed dignissim risus in quam tristique mollis. Nullam viverra convallis hendrerit. Phasellus bibendum risus in dignissim dapibus. Donec malesuada lobortis neque sit amet lacinia. Vivamus non tellus est. Sed vulputate ligula quis urna aliquam, quis egestas quam lacinia.

Suspendisse faucibus neque eget gravida sagittis. Aliquam erat augue, laoreet nec ornare a, scelerisque eu dolor. Vestibulum tempor magna dictum ligula auctor vestibulum. Mauris vel leo a enim volutpat egestas quis a lacus. In consequat ante massa, ut sagittis est ornare id. Sed nisi elit, vestibulum eu sagittis dictum, imperdiet quis magna. Maecenas velit augue, posuere et sodales sed, mollis eget magna. Integer accumsan lectus vitae libero porta scelerisque. Quisque magna ligula, malesuada id justo sit amet, tristique molestie massa. Vivamus tincidunt orci risus, eget facilisis neque ultricies vitae. Quisque finibus, massa nec luctus tincidunt, turpis augue scelerisque lacus, nec gravida enim lorem nec ipsum. Donec sit amet felis at ex varius lobortis. Proin blandit felis at risus sodales, nec hendrerit metus elementum. Maecenas vulputate sapien quis diam feugiat vulputate et ut turpis.
"""

    return render(request, 'template/article/article.html', {'title': title, 'author': author, 'article_text': article_text} )
