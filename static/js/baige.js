(function($) {
	$(document).ready(function() {



		// 志愿项目 Tab
		$(".activity .tab li").click(function() {
			$(this).siblings("li.active").removeClass("active");
			$(this).addClass("active");
			$(this).parent(".tab").siblings(".post-content").children(".posts.active").removeClass("active");
			$(this).parents(".activity").find("a.active").removeClass("active");
			$("." + $(this).attr("id")).addClass("active");
		});
		$(".prj-list li").mouseover(function() {
			refreshSlideBar($(this));
		});
		$(".prj-list li").mouseout(function() {
			refreshSlideBar($(".prj-list .active"));
		});

		// 更新Tab位置
		refreshSlideBar($(".prj-list .active"), 0);

		function refreshSlideBar(cur, d) {
				if (cur.length) {
					if (d == undefined) d = 300;
					var pos = cur.position();
					$(".slide-bar").stop();
					$(".slide-bar").animate({
						left: pos.left + "px",
						width: cur.width() + "px"
					}, d);
				}
			}
			// 志愿项目巨幕图片 IE8黑色遮罩
		if ($.browser.msie && parseInt($.browser.version) <= 8) {
			$(".prj-page .mid-image").prepend("<div class=\"before\"></div>");
		}

		// 博客侧边栏小工具跟随滚动
		var el = $(".widget-area");
		var el_r = $("#archive-content .page-content");
		var sidebarTop = el.length ? el.position().top + el.offset().top : 0;

		$(window).scroll(function(e) {
			if ($(window).scrollTop() - sidebarTop + 49 >= 0) {
				if ($(window).scrollTop() + el.height() > document.body.clientHeight - $(".site-footer").height() - 49 - 24 ) {
					el.css({
						position: "absolute",
						top: document.body.offsetHeight - $(".site-footer").height() - 24 - el.height() - sidebarTop
					});
				} else {
					el.css({
						position: "fixed",
						top: "49px"
					});
				}
			} else {
				el.css({
					position: "absolute",
					top: "auto"
				});
			}
		});


		// 博客标题logo
		$(".category-voice").find(".entry-logo").append($("<i class='fa fa-volume-up'></i>"));
		$(".category-download").find(".entry-logo").append($("<i class='fa fa-arrow-down'></i>"));
		$(".category-character").find(".entry-logo").append($("<i class='fa fa-user'></i>"));
		$(".category-training").find(".entry-logo").append($("<i class='fa fa-pencil-square-o'></i>"));
		$(".category-notice").find(".entry-logo").append($("<i class='fa fa-bullhorn'></i>"));
		$(".category-news").find(".entry-logo").append($("<i class='fa fa-newspaper-o'></i>"));

		// archive 导航栏 父目录 替换文本为 全部
		$(".archive .widget_categories > ul > li > a").html("全部");

		// commentForm input placeholder
		$(".comment-form-author #author").attr("placeholder", "您的姓名（必填）");
		$(".comment-form-email #email").attr("placeholder", "您的邮箱（不会公开，必填）");
		$(".comment-form-comment #comment").attr("placeholder", "在这里分享您的任何想法…");
	});
})(jQuery);
