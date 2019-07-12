# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


class RecipeView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = RecipeSerializer(recipes, many=True)
        return Response({"recipes": serializer.data})

    def post(self, request):
        recipe = request.data.get('recipe')
        # Create an article from the above data
        serializer = RecipeSerializer(data=recipe)
        if serializer.is_valid(raise_exception=True):
            recipe_saved = serializer.save()
        return Response({"success": "Recipe '{}' created successfully".format(recipe_saved.name)})

    def put(self, request, pk):
        saved_recipe = get_object_or_404(Recipe.objects.all(), pk=pk)
        data = request.data.get('recipe')
        serializer = RecipeSerializer(instance=saved_recipe, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            recipe_saved = serializer.save()
        return Response({"success": "Recipe '{}' updated successfully".format(recipe_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        recipe = get_object_or_404(Recipe.objects.all(), pk=pk)
        recipe.delete()
        return Response({"message": "Recipe with id `{}` has been deleted.".format(pk)}, status=204)
