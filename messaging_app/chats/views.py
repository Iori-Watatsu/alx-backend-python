from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from .permissions import IsOwner
from .permissions import IsParticipantOfConversation
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter
from .pagination import MessagePagination

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    permission_classes = [IsParticipantOfConversation]
    pagination_class = MessagePagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        # Ensure users can only see their own messages
        return Message.objects.filter(
            conversation__participants=self.request.user
        ).order_by('-created_at')

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Ensure users can only see their own conversations
        return Conversation.objects.filter(user=self.request.user)
        
    class ConversationViewSet(ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):

        return Conversation.objects.filter(participants=self.request.user)


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):

        return Message.objects.filter(
            conversation__participants=self.request.user
        )

    def perform_create(self, serializer):

        conversation = serializer.validated_data["conversation"]
        if not conversation.participants.filter(id=self.request.user.id).exists():
            raise PermissionDenied("You are not a participant of this conversation.")

        serializer.save(sender=self.request.user)

        