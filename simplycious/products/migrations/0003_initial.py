# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('products_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('products', ['Tag'])

        # Adding model 'Category'
        db.create_table('products_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('tagline', self.gf('django.db.models.fields.TextField')()),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'], null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('logo', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('products', ['Category'])

        # Adding model 'Product'
        db.create_table('products_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('logo', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('tagline', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('products', ['Product'])

        # Adding model 'Vote'
        db.create_table('products_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('products', ['Vote'])

        # Adding model 'ProductTag'
        db.create_table('products_producttag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Tag'])),
            ('include', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('products', ['ProductTag'])

        # Adding model 'Screenshot'
        db.create_table('products_screenshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('home', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('products', ['Screenshot'])

        # Adding model 'Video'
        db.create_table('products_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('home', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('products', ['Video'])

        # Adding model 'Presentation'
        db.create_table('products_presentation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('home', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('products', ['Presentation'])

        # Adding model 'CategoryTag'
        db.create_table('products_categorytag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Tag'])),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('imp', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('products', ['CategoryTag'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('products_tag')

        # Deleting model 'Category'
        db.delete_table('products_category')

        # Deleting model 'Product'
        db.delete_table('products_product')

        # Deleting model 'Vote'
        db.delete_table('products_vote')

        # Deleting model 'ProductTag'
        db.delete_table('products_producttag')

        # Deleting model 'Screenshot'
        db.delete_table('products_screenshot')

        # Deleting model 'Video'
        db.delete_table('products_video')

        # Deleting model 'Presentation'
        db.delete_table('products_presentation')

        # Deleting model 'CategoryTag'
        db.delete_table('products_categorytag')


    models = {
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tagline': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Tag']", 'through': "orm['products.CategoryTag']", 'symmetrical': 'False'})
        },
        'products.categorytag': {
            'Meta': {'object_name': 'CategoryTag'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Tag']"})
        },
        'products.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'tagline': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Tag']", 'through': "orm['products.ProductTag']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'products.producttag': {
            'Meta': {'object_name': 'ProductTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Tag']"})
        },
        'products.screenshot': {
            'Meta': {'object_name': 'Screenshot'},
            'home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'products.tag': {
            'Meta': {'object_name': 'Tag'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'products.video': {
            'Meta': {'object_name': 'Video'},
            'home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'products.vote': {
            'Meta': {'object_name': 'Vote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['products']